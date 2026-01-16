import requests
import json

URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "mistral-7b-instruct-v0.2"

prompt = """
You are a helpful assistant.

User: Say hello in one short sentence.
Assistant:
"""

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2,
    "max_tokens": 50
}

headers = {"Content-Type": "application/json"}

response = requests.post(URL, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response Text:")
print(response.text)