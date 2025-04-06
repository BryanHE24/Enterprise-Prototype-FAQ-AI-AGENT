from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from backend.vector_store import get_vector_store

vector_store = get_vector_store()
retriever = vector_store.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

def ask_question(query):
    return qa_chain({"query": query})