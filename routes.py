from fastapi.routing import APIRouter
from fastapi import UploadFile, File, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage
from pdfLoader import load_pdf
from vectorStore import vector_store
from chatController import rag_chain, llm
from chatController import chat, chat_with_pdf
import os
import tempfile

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Sube un PDF y lo procesa para agregarlo al vector store
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")
    
    # Crea un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        
    # Carga y procesa el pdf
    docs = load_pdf(temp_file.name)
        
    if not docs:
        raise HTTPException(status_code=500, detail="Error al procesar el PDF")
        
    # Agrega los documentos a la vector store
    vector_store.add_documents(docs)
        
    return {
        "status": "success",
        "message": f"PDF '{file.filename}' procesado exitosamente",
        "chunks": len(docs)
    }
    

@router.post("/answers")
async def chat_with_my_pdf(chat: chat):
    return await chat_with_pdf(chat)

@router.post("/chat")
async def chatBot(chat: chat):
    
    response = llm.invoke([
        SystemMessage(content="Eres un asistente que responde solo a preguntas basadas en la Segunda Guerra Mundial."),
        HumanMessage(content=chat.question)
    ])
    
    return response.content