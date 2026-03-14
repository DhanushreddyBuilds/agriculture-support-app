from google import genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

try:
    API_KEY = os.getenv("GEMINI_API_KEY")
    # Try with v1beta just in case
    client = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1beta'})
    
    print("Testing generate_content with gemini-1.5-flash (v1beta)...")
    response = client.models.generate_content(
        model='gemini-1.5-flash', 
        contents="Reply with 'AgroAI is Online'"
    )
    print("Response:", response.text)
    print("SUCCESS")

except Exception as e:
    print("\nERROR:", e)
