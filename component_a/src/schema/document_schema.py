from pydantic import BaseModel


class DocumentRequest(BaseModel):
    doc_id: str


class Document(BaseModel):
    content: str
    title: str
