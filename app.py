import streamlit as st
import os
import time
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Safety check
if not google_api_key or not groq_api_key:
    st.error("❌ Missing API keys. Please ensure your .env file has both GOOGLE_API_KEY and GROQ_API_KEY.")
    st.stop()

# Streamlit UI setup
st.set_page_config(page_title="LawGPT")
col1, col2, col3 = st.columns([1, 4, 1])
st.title("📚 Llama3-Powered Legal ChatBot (IPC Based)")
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ffd0d0;
    }
    div.stButton > button:active {
        background-color: #ff6262;
    }
    div[data-testid="stStatusWidget"] div button {
        display: none;
    }
    .reportview-container {
        margin-top: -2em;
    }
    #MainMenu, footer, .stDeployButton, #stDecoration, button[title="View fullscreen"] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Reset conversation
def reset_conversation():
    st.session_state.messages = []
    st.session_state.memory.clear()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        k=2,
        memory_key="chat_history",
        return_messages=True
    )

# Initialize embeddings and load vector store
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="AIzaSyCpQ06nKRaH-WWiObaphuAourbGL5Pw8sM"
)

db = FAISS.load_local("my_vector_store", embeddings, allow_dangerous_deserialization=True)
db_retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# Prompt template
prompt_template = """
<s>[INST]This is a chat template. As a legal chatbot, your primary objective is to provide accurate and concise information based on the user's questions. Do not generate your own questions and answers. Stick to the instructions provided, offering relevant context from the knowledge base while avoiding unnecessary details. If a question falls outside the context, avoid using chat history and rely only on your own knowledge base to respond. Prioritize professionalism, precision, and Indian Penal Code relevance.

CONTEXT: {context}
CHAT HISTORY: {chat_history}
QUESTION: {question}
ANSWER:
</s>[INST]
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question', 'chat_history'])

# Load the model from Groq
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")

# Set up Conversational QA chain
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    memory=st.session_state.memory,
    retriever=db_retriever,
    combine_docs_chain_kwargs={'prompt': prompt}
)

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

# Input box
input_prompt = st.chat_input("💬 Ask your legal question")

if input_prompt:
    with st.chat_message("user"):
        st.write(input_prompt)
    st.session_state.messages.append({"role": "user", "content": input_prompt})

    with st.chat_message("assistant"):
        with st.status("Thinking 💡...", expanded=True):
            result = qa.invoke(input=input_prompt)
            message_placeholder = st.empty()
            full_response = "\n\n\n"

            for chunk in result["answer"]:
                full_response += chunk
                time.sleep(0.02)
                message_placeholder.markdown(full_response + " ▌")

        st.button('🔁 Reset All Chat', on_click=reset_conversation)

    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
