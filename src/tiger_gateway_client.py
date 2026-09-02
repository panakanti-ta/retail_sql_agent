import requests
from src.config import GATEWAY_URL, GATEWAY_KEY, GATEWAY_MODEL

def call_llm(messages: list[dict]) -> str:
    if not GATEWAY_URL or not GATEWAY_KEY:
        raise ValueError("API Configuration missing. Please check TIGER_AI_GATEWAY_URL and TIGER_AI_GATEWAY_API_KEY in .env file.")
    headers = {"Authorization": f"Bearer {GATEWAY_KEY}", "Content-Type": "application/json"}
    payload = {"model": GATEWAY_MODEL, "messages": messages, "temperature": 0.0}
    response = requests.post(GATEWAY_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
