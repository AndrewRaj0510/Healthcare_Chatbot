import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

FAISS_INDEX_PATH = "data/processed/faiss_index.index"
DOCSTORE_PATH = "data/processed/docstore.pkl"

# Load vector store
index = faiss.read_index(FAISS_INDEX_PATH)

with open(DOCSTORE_PATH, "rb") as f:
    documents = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_documents(query, top_k=5):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        results.append(documents[idx])

    return results


if __name__ == "__main__":
    query = "What are the symptoms of glaucoma?"
    results = retrieve_documents(query)

    for i, doc in enumerate(results, 1):
        print(f"\n--- Result {i} ---\n")
        print(doc[:500])