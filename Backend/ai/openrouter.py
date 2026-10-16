import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing from .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def ask_openrouter(prompt: str) -> str:

    response = client.chat.completions.create(
        model="YOUR_FREE_MODEL",
        messages=[
            {
                "role": "system",
                "content": "You are SafeSpace AI, a helpful and safety-focused AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content