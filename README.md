

# SmartLawyer – AI-Powered Legal Assistant using RAG

**SmartLawyer** is an AI-powered legal assistant that leverages **Retrieval-Augmented Generation (RAG)** to provide answers to legal queries. This project enables users to interact with Indian legal documents and acts efficiently, retrieving relevant sections and generating context-aware answers.

---

## ✨ Features

* 📚 **Document Ingestion** – Supports multiple legal documents in PDF format (e.g., Companies Act, Labour Act, IPC)
* 🔍 **Semantic Search** – Uses FAISS for vector-based similarity search
* 🤖 **AI Answer Generation** – Combines retrieval with language models for accurate responses
* 🗂️ **Custom Knowledge Base** – Add or update legal documents easily
* 💾 **Persistence** – Stores vector indices for fast querying
* 🚀 **RAG Workflow** – Integrates document retrieval with natural language generation

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI / ML:** OpenAI GPT models (or compatible LLM), FAISS
* **File Handling:** PDF parsing & ingestion
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```plaintext
smartlawyer-using-rag/
├── app.py                  # Main Flask application
├── ingestion.py            # Script to process & index legal documents
├── index.faiss             # FAISS vector index for semantic search
├── index.pkl               # Pickled metadata for vector index
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .gitignore
├── README.md
├── assets/
│   └── PDFs/               # Legal documents (IPC, Companies Act, Labour Act, etc.)
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/abhishek9880/smartlawyer-using-rag.git
cd smartlawyer-using-rag
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env` (e.g., API keys for LLM service):

```env
OPENAI_API_KEY=<your-api-key>
```

---

## 🚀 Usage

1. **Ingest documents** into the knowledge base:

```bash
python ingestion.py
```

2. **Run the Flask application**:

```bash
python app.py
```

3. Open your browser and access the app at:

```
http://127.0.0.1:5000
```

4. **Ask legal questions** and receive AI-powered answers sourced from the ingested documents.

---

## 📄 Supported Documents

* Companies Act, 2013
* Labour Act
* IPC (Indian Penal Code)
* Copyright Rules, 1957
* COI (Certificate of Incorporation)
* Custom Acts (user can upload PDF documents)

---

## 🔑 Key Components

* **`ingestion.py`** – Handles PDF parsing, vector embedding, and FAISS index creation
* **`app.py`** – Flask application providing web interface and query handling
* **FAISS index** – Enables semantic search and fast retrieval of relevant legal sections
* **Environment Variables** – Secure API keys and credentials

---

## 📝 License

This project is licensed under the **MIT License**, allowing free usage, modification, and distribution.

---

## 👨‍💻 Author

**Abhishek Mishra**

* [GitHub](https://github.com/abhishek9880)
* [LinkedIn](https://www.linkedin.com/in/abhishek-mishra-49888123b)
* 📧 Email: [abhishekmmishra09896@gmail.com](mailto:abhishekmmishra09896@gmail.com)

---

✅ **Summary:**
SmartLawyer combines **AI and legal knowledge retrieval** using the **RAG architecture**, enabling users to query legal documents efficiently and accurately. The project is modular, scalable, and suitable for legal research or automated legal assistance.

