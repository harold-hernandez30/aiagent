from google.genai import types
from functions.get_files_info_schema import schema_get_files_info
from functions.get_file_content_schema import get_file_content_schema
from functions.write_file_schema import write_file_schema
from functions.run_python_schema import run_python_schema

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
available_functions = types.Tool (
    function_declarations=[
        schema_get_files_info,
        get_file_content_schema,
        write_file_schema,
        run_python_schema
    ]
)

