from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

from schema.document_schema import DocumentRequest, Document
from schema.llm_schema import Turn

from utils.database import Database
from utils.llm import LLM

PORT_NUM = os.environ.get("COMPONENT_A_CONTAINER_PORT", 8000)

db = Database()
llm = LLM()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all
    allow_credentials=False,
    allow_methods=["*"],  # Allow all
    allow_headers=["*"],  # Allow all
)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    """Health check"""
    return {"status": "healthy"}


@app.post("/retrieve_document")
async def retrieve_document(doc_req: DocumentRequest) -> Document:
    return db.get_document(doc_id=doc_req.doc_id)


@app.post("/chat")
async def chat(query: list[Turn]) -> Turn:
    return llm.chat(query)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(PORT_NUM),
        reload=True,  # Enable hot reload for debugging purpose
    )
