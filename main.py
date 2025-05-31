import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv, exit

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


if len(argv) == 1:
    print("error: please provide prompt")
    exit(1)

user_prompt = argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

client = genai.Client(api_key=api_key)
contentResponse = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(contentResponse.text)
print(f"Prompt tokens: {contentResponse.usage_metadata.prompt_token_count}")
print(f"Response tokens: {contentResponse.usage_metadata.candidates_token_count}")