from google.genai.types import FunctionDeclaration, Schema, Type

schema_get_files_info = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "directory": Schema(
                type=Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)