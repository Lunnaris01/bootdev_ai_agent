import os
import sys
from dotenv import load_dotenv

if len(sys.argv)<2:
    print("Please provide the prompt: python main.py \"This is my question to the AI!\"")
    sys.exit(1)
contents=sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)


response = client.models.generate_content(model="gemini-2.0-flash-001", contents=contents)
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(response.text)
