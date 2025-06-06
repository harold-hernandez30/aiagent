from functions.escape_check import validate_escape
from os.path import exists, isdir, join
from os import makedirs

def write_file(working_directory, file_path, content):
    target_file_abs_path = validate_escape(working_directory, file_path)

    if target_file_abs_path is None:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    dirs_path_arr = target_file_abs_path.split("/")
    dirs_path_arr = dirs_path_arr[:len(dirs_path_arr) - 1]
    dirs_only = join('/', *dirs_path_arr)

    if not exists(dirs_only):
        makedirs(dirs_only)

    file_operation = "w"
    if not exists(target_file_abs_path):
        file_operation = "x"

    try: 
        with open(target_file_abs_path, file_operation) as f:
            content_size = f.write(content)
            return f'Successfully wrote to "{file_path}" ({content_size} characters written)'

    except Exception as e:
        return f'Error: "{file_path}" could not be written to'
