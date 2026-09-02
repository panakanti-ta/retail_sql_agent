import requests
from src.config import GATEWAY_URL, GATEWAY_KEY, GATEWAY_MODEL

def call_llm(messages: list[dict]) -> str:
    if not GATEWAY_URL or not GATEWAY_KEY:
        raise ValueError(
            "API configuration missing. Set the user environment variables "
            "TIGER_AI_GATEWAY_URL and TIGER_AI_GATEWAY_API_KEY."
        )
    headers = {
        "Authorization": f"Bearer {GATEWAY_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"model": GATEWAY_MODEL, "messages": messages, "temperature": 0.0}
    response = requests.post(
        GATEWAY_URL,
        headers=headers,
        json=payload,
        timeout=60,
    )
    response.raise_for_status()

    body = response.json()
    if not isinstance(body, dict):
        raise ValueError(
            "Unexpected LLM response: expected a JSON object with "
            f"'choices', received {type(body).__name__}: {body!r}"
        )

    choices = body.get("choices")

    if not isinstance(choices, list) or not choices:
        raise ValueError(f"Unexpected LLM response: {body}")

    if not isinstance(choices[0], dict):
        raise ValueError(f"Unexpected LLM choice: {choices[0]!r}")

    message = choices[0].get("message", {})
    if not isinstance(message, dict):
        raise ValueError(f"Unexpected LLM message: {message!r}")

    content = message.get("content")

    if not isinstance(content, str) or not content.strip():
        raise ValueError(f"LLM response has no usable content: {body}")

    return content
