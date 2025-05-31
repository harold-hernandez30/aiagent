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

args = argv[1:]

def has_flag(flag):
    if flag in argv:
        return True
    
    return False
        
is_verbose = has_flag("--verbose")
if is_verbose:
    args.remove("--verbose")

user_prompt = " ".join(args)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

client = genai.Client(api_key=api_key)
contentResponse = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
if is_verbose:
    verbose_messages = [
        f"Working on: {user_prompt}",
        f"Prompt tokens: {contentResponse.usage_metadata.prompt_token_count}",
        f"Response tokens: {contentResponse.usage_metadata.candidates_token_count}"
    ]
    for log in verbose_messages:
        print(log)
print("Response:")
print(contentResponse.text)