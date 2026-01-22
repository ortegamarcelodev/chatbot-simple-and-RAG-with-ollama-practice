from fastapi import HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from retriever import retriever

llm = ChatOllama(model="llama3.2:latest", temperature=0.7)

class chat(BaseModel):
    question: str

template = """
Eres un asistente que ayuda a responder 
preguntas basadas en los siguientes documentos proporcionados. 
Utiliza solo la información contenida en estos documentos para formular tu respuesta. 
Si la información no está disponible en los documentos, responde con 
"No tengo suficiente información para responder a esa pregunta."

CONTEXTO: {context}

PREGUNTA: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs: list):
    return "\n\n".join([doc.page_content for doc in docs])

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

async def chat_with_pdf(chat: chat):
    """
    Responde preguntas basadas en los PDFs cargados usando RAG
    """
    
    try:
        response = rag_chain.invoke(chat.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")