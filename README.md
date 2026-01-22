# 🤖 RAG Chat con PDFs - Práctica IA

Proyecto de práctica que implementa un sistema de chat con inteligencia artificial e integrado en una API usando **RAG (Retrieval-Augmented Generation)** para consultar documentos PDF y un chat conversacional básico sobre la Segunda Guerra Mundial y todo sobre un servidor creado con FastAPI.

## ✨ Características

- 📄 **Carga y procesa archivos PDF** usando embeddings vectoriales
- 💬 **Chat con RAG**: Responde preguntas basadas en el contenido de los PDFs cargados
- 🗨️ **Chat simple**: Conversación sobre temas de la Segunda Guerra Mundial
- 🔍 **Vector Store persistente**: Los PDFs procesados se almacenan localmente
- ⚡ **API REST con FastAPI**: Endpoints para subir PDFs y hacer consultas

## 🛠️ Tecnologías

- **FastAPI** - Framework web
- **LangChain** - Orquestación de LLMs y RAG
- **Ollama** - LLM local (llama3.2)
- **ChromaDB** - Base de datos vectorial
- **PyPDF** - Procesamiento de PDFs

## 📋 Requisitos Previos

- Python 3.8+
- [Ollama](https://ollama.ai/) instalado con el modelo `llama3.2:latest` y `nomic-embed-text:latest`

```bash
# Instalar modelos de Ollama
ollama pull llama3.2:latest
ollama pull nomic-embed-text:latest
```

## 🚀 Instalación

### 1. Crear carpeta y clonar el repositorio

```bash
mkdir practica-ia
cd practica-ia
git clone https://github.com/ortegamarcelodev/chatbot-simple-and-RAG-with-ollama-practice.git
```

### 2. Crear entorno virtual

**Opción A: Con `uv` (recomendado si lo tienes instalado)**

```bash
uv venv
```

**Opción B: Con Python estándar**

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**En Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

**En Windows (CMD):**

```bash
.venv\Scripts\activate.bat
```

**En Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

**Con `uv`:**

```bash
uv pip install -r requirements.txt
```

**Con pip estándar:**

```bash
pip install -r requirements.txt
```

## 🎮 Uso

### Iniciar el servidor

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

### 📚 Documentación de la API

Una vez iniciado el servidor, visita:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Endpoints

### 1. Subir PDF

Carga un archivo PDF y lo procesa para el RAG.

```http
POST /upload-pdf
Content-Type: multipart/form-data

file: <archivo.pdf>
```

**Respuesta:**
```json
{
  "status": "success",
  "message": "PDF 'archivo.pdf' procesado exitosamente",
  "chunks": 42
}
```

### 2. Chat con RAG (Consulta PDFs)

Realiza preguntas sobre los PDFs cargados.

```http
POST /answers
Content-Type: application/json

{
  "question": "¿Cuál es el tema principal del documento?"
}
```

**Respuesta:**
```json
{
  "answer": "El documento trata sobre..."
}
```

### 3. Chat Simple

Conversación sobre la Segunda Guerra Mundial sin contexto de PDFs.

```http
POST /chat
Content-Type: application/json

{
  "question": "¿Cuándo empezó la Segunda Guerra Mundial?"
}
```

**Respuesta:**
```
La Segunda Guerra Mundial comenzó el 1 de septiembre de 1939...
```

## 📁 Estructura del Proyecto

```
practica-ia/
├── main.py              # Punto de entrada de la aplicación
├── routes.py            # Definición de endpoints
├── chatController.py    # Lógica del RAG chain
├── pdfLoader.py         # Carga y procesamiento de PDFs
├── vectorStore.py       # Configuración del vector store
├── retriever.py         # Recuperación de documentos
├── requirements.txt     # Dependencias
├── .gitignore          # Archivos ignorados por git
└── vector_store/       # Almacenamiento persistente (generado)
```

## 🧪 Ejemplo de Uso

1. **Subir un PDF:**
   ```bash
   curl -X POST "http://localhost:8000/upload-pdf" \
     -F "file=@documento.pdf"
   ```

2. **Hacer una pregunta sobre el PDF:**
   ```bash
   curl -X POST "http://localhost:8000/answers" \
     -H "Content-Type: application/json" \
     -d '{"question": "¿De qué trata el documento?"}'
   ```

3. **Chat simple:**
   ```bash
   curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"question": "¿Qué fue el Día D?"}'
   ```

## 📝 Notas

- Los PDFs procesados se almacenan en la carpeta `vector_store/` para consultas futuras
- El chat simple está limitado a preguntas sobre la Segunda Guerra Mundial
- Asegúrate de tener Ollama corriendo en segundo plano

## 🤝 Contribuciones

Este es un proyecto de práctica educativo. Siéntete libre de hacer fork y experimentar!

## 📄 Licencia

MIT

---
