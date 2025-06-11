from google.genai.types import FunctionDeclaration, Schema, Type

run_python_schema = FunctionDeclaration(
    name="run_python_file",
    description="Run the python script on the specified file_path",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The python file to run.",
            )
        },
    ),
)