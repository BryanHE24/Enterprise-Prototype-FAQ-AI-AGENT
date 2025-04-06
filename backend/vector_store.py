from backend.document_loader import load_documents
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader, Docx2txtLoader

DB_DIR = "db"
DATA_DIR = "data"

# Load documents, embed them, and store in Chroma DB
def get_vector_store():
    documents = load_documents(DATA_DIR)
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(documents, embeddings, persist_directory=DB_DIR)
