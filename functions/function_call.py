from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from google.genai import types

functions_map = {
    "get_file_content": get_file_content,
    "get_files_info":get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
}

def function_call(function_call_part, verbose=False):

    function_name = function_call_part.name
    function_args = function_call_part.args
    
    if (verbose):
        print(f'Calling function: {function_name}({function_args})')
    else:
        print(f" - Calling function: {function_name}")

    actual_function = functions_map[function_name]

    if (actual_function is None):
        return types.Content(
            role="tool", 
            parts=[ types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
                )
            ],
    )
    
    function_result = actual_function('./calculator', **function_call_part.args)

    return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
            )
        ],
    )
