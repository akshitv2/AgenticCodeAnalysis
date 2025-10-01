from crewai import LLM
import os
from dotenv import load_dotenv

gemini = LLM(
    model='gemini/gemini-2.5-flash',
    temperature=0.7,
    api_key=""
)