from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

PORT_NUM = os.environ.get("COMPONENT_B_CONTAINER_PORT", 8000)

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


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(PORT_NUM),
        reload=True,  # Enable hot reload for debugging purpose
    )
