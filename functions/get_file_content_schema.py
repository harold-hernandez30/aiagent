from google.genai.types import FunctionDeclaration, Schema, Type


get_file_content_schema = FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of the files",
    parameters= Schema(
        type=Type.OBJECT,
        properties={
            "file": Schema(
                type=Type.STRING,
                description="The file to read the content from"
            )
        }
    )
)