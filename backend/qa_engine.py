from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from backend.vector_store import get_vector_store

# Load vector store and create retriever
vector_store = get_vector_store()
retriever = vector_store.as_retriever()

# Create QA chain using GPT-4 and retriever
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Main question-answering function
def ask_question(query):
    return qa_chain({"query": query})
