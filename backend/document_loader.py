import os
from langchain.document_loaders import TextLoader, PyMuPDFLoader, Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter

def load_documents(directory):
    docs = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
        elif file.endswith(".pdf"):
            docs.extend(PyMuPDFLoader(path).load())
        elif file.endswith(".docx"):
            docs.extend(Docx2txtLoader(path).load())
    return CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
