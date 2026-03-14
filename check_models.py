import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

try:
    API_KEY = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=API_KEY)
   
    print("Listing available models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")

except Exception as e:
    print("\nERROR:", e)
