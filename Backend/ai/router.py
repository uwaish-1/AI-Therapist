import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()


# --------------------------------------------------
# Gemini
# --------------------------------------------------

gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2,
)


# --------------------------------------------------
# Groq
# --------------------------------------------------

groq = ChatOpenAI(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    temperature=0.2,
)


# --------------------------------------------------
# OpenRouter
# --------------------------------------------------

openrouter = ChatOpenAI(
    model="YOUR_OPENROUTER_FREE_MODEL",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.2,
)


# --------------------------------------------------
# AI Router
# Gemini → Groq → OpenRouter
# --------------------------------------------------

ai_router = gemini.with_fallbacks(
    [groq, openrouter]
)