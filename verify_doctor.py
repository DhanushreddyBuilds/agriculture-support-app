import sys
import os
import google.generativeai as genai
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app import generate_response

# Overwrite sys.stdout to handle utf-8
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Testing 'Doctor' Persona with query: 'My tomato plant has yellow leaves'")
response = generate_response("Tomato", "leaf", False, "My tomato plant has yellow leaves")
print("\n--- RESPONSE ---\n")
print(response)
print("\n----------------\n")
