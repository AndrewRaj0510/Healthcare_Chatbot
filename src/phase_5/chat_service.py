from src.phase_3.retrieve import retrieve_documents
from src.phase_3.rag_context_builder import build_rag_context
from src.phase_4.llm_client import call_llm

def generate_chat_response(question: str) -> str:
    # Step 1: Retrieve relevant medical documents
    docs = retrieve_documents(question)

    if not docs:
        return (
            "I’m sorry, I could not find relevant medical information for your question. "
            "Please consult a qualified healthcare professional for guidance."
        )

    # Step 2: Build RAG context
    context = build_rag_context(docs)

    # Step 3: Call local LLM via LM Studio
    answer = call_llm(context, question)

    return answer