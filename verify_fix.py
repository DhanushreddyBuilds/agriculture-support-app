import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

models_to_try = [
    'models/gemini-2.0-flash-lite-001',
    'gemini-2.0-flash',
    'gemini-pro',
    'gemini-1.5-pro-latest'
]

print("Testing Multi-Model Fallback Logic...")

for model_name in models_to_try:
    try:
        print(f"Attempting: {model_name}")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello plant doctor, my tomatoes are dying.")
        
        if response and response.text:
            print(f"\nSUCCESS with {model_name}!\nRESPONSE:\n{response.text[:100]}...")
            break
            
    except Exception as e:
        print(f"FAILED ({model_name}): {e}")
