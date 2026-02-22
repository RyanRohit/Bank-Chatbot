import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(context, query):
    prompt = f"""
You are a banking assistant.

Answer strictly from the context.
Do not make up information.
If not found, say:
"Please contact customer support."

Context:
{context}

Question:
{query}

Answer:
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]