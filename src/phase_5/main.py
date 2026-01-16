from fastapi import FastAPI
from src.phase_5.schemas import ChatRequest, ChatResponse
from src.phase_5.chat_service import generate_chat_response

app = FastAPI(
    title="Healthcare RAG Chatbot API",
    description="Backend API for healthcare information chatbot",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    answer = generate_chat_response(request.question)
    return ChatResponse(answer=answer)