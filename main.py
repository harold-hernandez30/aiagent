import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv, exit
from config import system_prompt, available_functions
from functions.function_call import function_call

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
config = types.GenerateContentConfig(tools=[available_functions], 
                                     system_instruction=system_prompt)
client = genai.Client(api_key=api_key)

agent_loop_finalized = False
for control in range(20):
    contentResponse = client.models.generate_content(model="gemini-2.0-flash-001", 
                                                 contents=messages, 
                                                 config=config)
    
    if agent_loop_finalized:
        break

    for candidate in contentResponse.candidates:
        control += 1

        if control >= 20:
            print("Final response")
            print(contentResponse.text)
            agent_loop_finalized = True
            break
        messages.append(candidate.content)


        if contentResponse.function_calls is None:
            print("Final response")
            print(contentResponse.text)
            agent_loop_finalized = True
            break
        else:    
            function_calls_part = contentResponse.function_calls

            for funcation_call_part in function_calls_part:
                try:

                    function_call_result = function_call(funcation_call_part, is_verbose)
                    messages.append(function_call_result)
                    if (is_verbose):
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                except Exception as e:
                    print(f'Exception raised: {e}')

if is_verbose:
    verbose_messages = [
        f"Working on: {user_prompt}",
        f"Prompt tokens: {contentResponse.usage_metadata.prompt_token_count}",
        f"Response tokens: {contentResponse.usage_metadata.candidates_token_count}"
    ]
    for log in verbose_messages:
        print(log)

