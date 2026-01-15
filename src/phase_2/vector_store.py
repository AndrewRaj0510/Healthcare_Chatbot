import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

DOCUMENT_PATH = "data/processed/healthcare_documents.txt"
FAISS_INDEX_PATH = "data/processed/faiss_index.index"
DOCSTORE_PATH = "data/processed/docstore.pkl"

# Load documents
with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()

documents = [doc.strip() for doc in raw_text.split("=" * 80) if doc.strip()]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents, show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, FAISS_INDEX_PATH)

# Save documents
with open(DOCSTORE_PATH, "wb") as f:
    pickle.dump(documents, f)

print("✅ FAISS index and document store saved")
print("Total vectors:", index.ntotal)