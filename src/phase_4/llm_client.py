import requests

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "mistral-7b-instruct-v0.2"


def build_prompt(context: str, question: str) -> str:
    """
    Build a single-user prompt compatible with LM Studio.
    System instructions are merged into the user content.
    """

    return f"""
You are a healthcare information assistant.

Rules you MUST follow:
- You may suggest possible conditions but MUST NOT confirm a diagnosis.
- Always use non-definitive language such as "may", "could", or "might".
- Do NOT prescribe medication dosages.
- Do NOT provide emergency instructions.
- Always recommend consulting a qualified doctor.
- Keep language simple and suitable for the general public.

Response format (STRICT):

Possible explanation:
<general, non-confirming explanation>

General care suggestions:
- <general advice only>

Important:
This information is for educational purposes only.
Please consult a qualified healthcare professional.

Medical Reference:
{context}

User Question:
{question}
"""


def call_llm(context: str, question: str) -> str:
    """
    Call LM Studio local server and return assistant response.
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": build_prompt(context, question)
            }
        ],
        "temperature": 0.3,
        "max_tokens": 512
    }

    response = requests.post(LM_STUDIO_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()