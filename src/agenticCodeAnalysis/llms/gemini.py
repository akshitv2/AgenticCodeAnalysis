from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GOOGLE_API_KEY")

gemini = LLM(
    model='gemini/gemini-2.5-flash',
    temperature=0.7,
    api_key=GEMINI_KEY
)