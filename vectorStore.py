from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model="nomic-embed-text:latest")

vector_store = Chroma(
    embedding_function=embedding_model,
    persist_directory="./vector_store",
    collection_name="documents"
)
