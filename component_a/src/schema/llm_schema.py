from pydantic import BaseModel


class Turn(BaseModel):
    role: str  # Either system, assistent or user
    content: str
