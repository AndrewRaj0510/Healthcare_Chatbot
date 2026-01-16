from src.phase_3.retrieve import retrieve_documents
from src.phase_3.rag_context_builder import build_rag_context
from src.phase_4.llm_client import call_llm

query = "I have blurry vision and sensitivity to light. What could it be?"

docs = retrieve_documents(query)
context = build_rag_context(docs)

response = call_llm(context, query)

print("\n=== CHATBOT RESPONSE ===\n")
print(response)