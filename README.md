# 🏥 Healthcare Information Chatbot (RAG-based, Local LLM)

A **local, privacy-friendly healthcare information chatbot** built using **Retrieval-Augmented Generation (RAG)** with **Mistral 7B Instruct (LM Studio)**.  
The chatbot provides **educational medical information**, suggests **possible conditions without confirming diagnoses**, and always recommends consulting a qualified healthcare professional.

---

## ⚠️ Medical Disclaimer

> This chatbot is for **educational purposes only**.  
> It does **not provide medical diagnoses**, does **not prescribe medications**, and does **not replace professional medical advice**.  
> Always consult a qualified doctor or healthcare professional for diagnosis and treatment.

---

## 🎯 Project Objectives

- Build a **healthcare-focused chatbot** for the general public
- Use **RAG instead of fine-tuning**
- Run **entirely locally** (privacy-preserving)
- Enforce **medical safety & ethical constraints**
- Provide a clean **UI + API architecture**

---

## 🧠 Key Features

- ✅ Local LLM via **LM Studio (Mistral 7B Instruct v0.2)**
- ✅ Healthcare Q&A dataset–driven retrieval
- ✅ Vector search using embeddings
- ✅ Medical safety guardrails (non-diagnostic)
- ✅ FastAPI backend
- ✅ Gradio chat UI
- ✅ Modular, phase-wise project structure

---

## 🧩 Architecture Overview

```
User
↓
Gradio UI
↓
FastAPI Backend
↓
Retriever
↓
Vector Database
↓
Healthcare Dataset
↓
LM Studio (Mistral 7B Instruct)
↓
Safe Medical Response
```

---

## 📁 Project Structure

```
Healthcare_Chatbot/
│
├── data/
├── src/
│   ├── phase_1/      # Dataset loading & inspection
│   ├── phase_2/      # Text preprocessing & chunking
│   ├── phase_3/      # Embeddings, vector search, retrieval
│   ├── phase_4/      # LM Studio integration & prompting
│   ├── phase_5/      # FastAPI backend
│   ├── phase_6/      # Gradio UI
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
uvicorn src.phase_5.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### ✅ Phase 6 — UI (Gradio)

- Built interactive chat UI
- Integrated with FastAPI backend
- Message history handling
- Enforced response structure
- Strong medical disclaimers
- Disabled empty submissions

Run server:

```bash
python -m src.phase6_ui.gradio_app
```

Open -> http://127.0.0.1:7860
---

## 🛡️ Medical Safety & Ethics

The chatbot is designed to:
- ❌ Never confirms a diagnosis
- ❌ Never provides medication dosages
- ❌ Never gives emergency instructions
- ✅ Uses non-definitive language (“may”, “could”)
- ✅ Always recommends consulting a doctor
- ✅ Provides general lifestyle / care suggestions only

Safety was tested against:
- Diagnosis confirmation prompts
- Medication dosage requests
- Emergency scenarios
- Mental health–related prompts

This is enforced via **prompt design**, not fine‑tuning.

---

## ▶️ How to Run the Project

- Start LM Studio
- Load **Mistral 7B Instruct v0.2**
- Start FastAPI Backend
- Start Gradio UI
- Chat with the assistant

---

## 🧰 Tech Stack

* **Python 3.10+**
* **FastAPI** – backend API
* **LM Studio** – local LLM server
* **Mistral‑7B Instruct v0.2** – language model
* **Sentence Transformers** – embeddings
* **FAISS / Vector DB** – semantic retrieval

---

## ⚠️ Disclaimer

This chatbot is for **educational purposes only**. It is **not a substitute for professional medical advice, diagnosis, or treatment**. Always seek the advice of a qualified healthcare provider.

---

## 👨‍💻 Author

Built as an **applied NLP + LLM systems project** using local inference and RAG principles.

## Future Work

- Streamlit UI alternative
- Dockerization
- Cloud deployment
- Better medical entity filtering