import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from backend.document_loader import load_documents

DB_DIR = "db"
DATA_DIR = "data"

# Load documents, embed them, and store in Chroma DB
def get_vector_store():
    documents = load_documents(DATA_DIR)
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(documents, embeddings, persist_directory=DB_DIR)
