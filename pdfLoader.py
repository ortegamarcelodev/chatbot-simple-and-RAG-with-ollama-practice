from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        docs = splitter.split_documents(pages)
        return docs
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []