
from os import listdir
from os.path import isdir, getsize, isfile, abspath, join, commonpath
import traceback

def get_file_content(working_directory, file):
    try:
        target_file_full_path = no_escape(working_directory, file)
        
        if target_file_full_path is None:
          return f'Error: "{file}" tried to escape'
        
        MAX_CHARS = 10000

        with open(target_file_full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if getsize(target_file_full_path) >= MAX_CHARS:
                return append_truncated_message(file_content_string, file)
            
            return file_content_string
    except Exception as e:
        return f'Error: something went wrong: {e}. \n Stacktrace: \n {traceback.format_exc()}'
        
def append_truncated_message(content, file):
    return content + f'[...File "{file}" truncated at 10000 characters]'

def no_escape(working_directory, file):
    abs_path_working_dir = abspath(working_directory)
    abs_path_target_file = abspath(join(working_directory, file))
    common_path = commonpath([abs_path_working_dir, abs_path_target_file])
    if common_path == abs_path_working_dir:
        return abs_path_target_file
    
    return None