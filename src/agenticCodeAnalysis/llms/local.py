from crewai import LLM
import os
from dotenv import load_dotenv

local_llm = LLM(
    model='openai/llama-3',
    temperature=0.7,
    api_key="",
    base_url="http://192.168.1.15:1234/v1/"
)