import requests
import json
from src.phase_4.prompt_templates import SYSTEM_PROMPT

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "mistral-7b-instruct-v0.2"

def call_llm(context, user_question):
    combined_prompt = f"""
{SYSTEM_PROMPT}

Medical References:
{context}

User Question:
{user_question}

Assistant:
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": combined_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 512
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(
        LM_STUDIO_URL,
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code != 200:
        print("LM Studio error:")
        print(response.text)
        response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]