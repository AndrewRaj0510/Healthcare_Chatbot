from sentence_transformers import SentenceTransformer
import pandas as pd

DOCUMENT_PATH = "data/processed/healthcare_documents.txt"

# Load documents
with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()

documents = raw_text.split("=" * 80)

documents = [doc.strip() for doc in documents if doc.strip()]
print(f"📄 Loaded {len(documents)} documents")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents, show_progress_bar=True)

print("✅ Embeddings generated")
print("Embedding shape:", embeddings.shape)