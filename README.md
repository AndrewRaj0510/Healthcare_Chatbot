# 🏥 Healthcare RAG Chatbot (Local LLM)

A **local, privacy‑preserving healthcare chatbot** built using **Retrieval‑Augmented Generation (RAG)** and **Mistral‑7B Instruct v0.2** running in **LM Studio**.
The chatbot provides **educational medical information**, suggests **possible conditions**, and **always advises consulting a qualified healthcare professional**. It does **not confirm diagnoses**.

---

## 🚀 Project Status

✅ **Phase 1–5 Completed**
🔜 UI, tone refinement, and safety enhancements planned

Current capabilities:

* Local LLM inference (no cloud APIs)
* Vector‑based medical document retrieval
* Safe medical prompt enforcement
* FastAPI backend with `/chat` endpoint

---

## 🧠 Key Design Principles

* ❌ No medical diagnosis confirmation
* ✅ Predictive language only ("may", "could", "possible")
* ✅ General treatment & care suggestions
* ⚠️ Always recommend consulting a doctor
* 🔒 Fully local (LM Studio + local embeddings)

---

## 🧩 Architecture Overview

```
User
  ↓
FastAPI (/chat)
  ↓
Retriever (Vector DB)
  ↓
RAG Context Builder
  ↓
Mistral 7B (LM Studio)
  ↓
Safe Medical Response
```

---

## 📁 Project Structure

```
Healthcare_Chatbot/
│
├── src/
│   ├── phase1_data/            # Dataset loading & inspection
│   ├── phase2_processing/      # Text preprocessing & chunking
│   ├── phase3_retrieval/       # Embeddings, vector search, retrieval
│   ├── phase4_llm/             # LM Studio integration & prompting
│   ├── phase5_api/             # FastAPI backend
│
├── lmstudio_test.py            # Standalone LM Studio test
├── README.md
└── .gitignore
```

---

## 🧪 Dataset

* Healthcare Question‑Answer dataset
* Shape: **(16,412 rows × 4 columns)**
* Contains some diagnostic‑flagged answers (handled via prompting)
* Target audience: **General Public**

---

## 🧠 Phase Breakdown

### ✅ Phase 1 — Data Understanding

* Loaded and inspected healthcare QA dataset
* Identified diagnostic‑sensitive responses
* Defined safety requirements

---

### ✅ Phase 2 — Text Processing

* Cleaned and normalized medical text
* Chunked documents for retrieval
* Prepared data for embeddings

---

### ✅ Phase 3 — Retrieval (RAG)

* Used `sentence-transformers/all-MiniLM-L6-v2`
* Created vector database (local)
* Implemented semantic search for relevant medical references

---

### ✅ Phase 4 — LLM Integration (LM Studio)

* Model: **Mistral‑7B Instruct v0.2**
* Running locally via **LM Studio**
* Implemented medical safety prompt
* Adapted prompting for GGUF models (no `system` role)
* End‑to‑end RAG → LLM pipeline verified

Standalone test:

```bash
python lmstudio_test.py
```

---

### ✅ Phase 5 — FastAPI Backend

* Built FastAPI backend
* Endpoints:

  * `GET /health`
  * `POST /chat`
* `/chat` connects:

  * Retrieval
  * Context builder
  * LM Studio inference

Run server:

```bash
uvicorn src.phase5_api.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🛡️ Medical Safety Prompting

The chatbot:

* Suggests possible conditions only
* Avoids definitive language
* Does not prescribe medication
* Refers users to healthcare professionals

This is enforced via **prompt design**, not fine‑tuning.

---

## 🧰 Tech Stack

* **Python 3.10+**
* **FastAPI** – backend API
* **LM Studio** – local LLM server
* **Mistral‑7B Instruct v0.2** – language model
* **Sentence Transformers** – embeddings
* **FAISS / Vector DB** – semantic retrieval

---

## 🔜 Next Planned Phases

* 🎨 Phase 6: UI (Gradio / Streamlit)
* 🧠 Phase 6.5: Tone refinement & safety scoring
* 📦 Phase 7: Project polish (docs, diagrams, deployment notes)

---

## ⚠️ Disclaimer

This chatbot is for **educational purposes only**. It is **not a substitute for professional medical advice, diagnosis, or treatment**. Always seek the advice of a qualified healthcare provider.

---

## 👨‍💻 Author

Built as an **applied NLP + LLM systems project** using local inference and RAG principles.
