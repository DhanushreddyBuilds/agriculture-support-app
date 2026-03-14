import requests
import json

try:
    print("Testing Root Endpoint...")
    response = requests.get("http://127.0.0.1:5000/")
    print(f"Root Status: {response.status_code}")
except Exception as e:
    print(f"Root Error: {e}")

try:
    print("\nTesting Chat Endpoint...")
    headers = {'Content-Type': 'application/json'}
    data = {'message': 'hello'}
    response = requests.post("http://127.0.0.1:5000/chat", headers=headers, json=data)
    print(f"Chat Status: {response.status_code}")
    print(f"Chat Response: {response.text}")
except Exception as e:
    print(f"Chat Error: {e}")
