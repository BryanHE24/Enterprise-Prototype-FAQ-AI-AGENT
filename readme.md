# 🧠 Enterprise FAQ AI Agent

An intelligent customer support prototype powered by OpenAI and LangChain. Ask your enterprise-related FAQs and get instant, AI-generated answers.

## ✨ Features

- 🔍 Natural language search over internal documents
- 📄 Supports `.txt`, `.pdf`, and `.docx` files
- 💬 Streamlit frontend with quick suggestions
- 🔐 Secure `.env` config for API keys
- 🧠 Powered by LangChain + GPT-4

---

## 🗂️ Project Structure
enterprise-faq-ai-agent/
├── backend/ # Flask API + LangChain logic
│   ├── app.py
│   ├── document_loader.py
│   ├── qa_engine.py
│   ├── vector_store.py
│   ├── __init__.py
│   └── data/ # FAQ dataset
│       └── faq.txt
├── frontend/ # Streamlit UI
│   └── app.py
├── .env # Environment config 
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/enterprise-faq-ai-agent.git
cd enterprise-faq-ai-agent
```

### 2. Create a virtual environment
```bash
python -m venv myen
source myen/bin/activate  # On Windows: myen\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up environment
Create a .env file in the root with your OpenAI key:
```bash
OPENAI_API_KEY=sk-...
```

## 🧠 Running the App
### 1. Start the backend (Flask API)
```bash
cd backend
python app.py
```
The API will run at http://localhost:5000

### 2. Start the frontend (Streamlit)
```bash
cd frontend
streamlit run app.py
```
Access the app at http://localhost:8501

### 📦 FAQ Dataset
The app is currently trained on faq.txt under backend/data/. You can add more .pdf or .docx files to expand knowledge coverage.

### Built With
- OpenAI GPT-4
- LangChain
- Streamlit
- ChromaDB
- Flask

### 🛡️ Security Notes
- Store your .env file securely and never commit it.
- Backend does not yet handle auth — avoid exposing it publicly without protection.