from google.genai.types import FunctionDeclaration, Schema, Type

write_file_schema = FunctionDeclaration(
    name="write_file",
    description="Write the content specified in the argument and write to the file_path specified",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The file path to read and write to.",
            ),
            "content": Schema(
                type=Type.STRING,
                description="The content to write on the file_path."
            )
        },
    ),
)