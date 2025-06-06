
from os import listdir
from os.path import isdir, getsize, isfile, abspath, join, commonpath
from functions.escape_check import validate_escape
import traceback

def get_files_info(working_directory, directory=None):

    try:

        target_dir = validate_escape(working_directory, directory)

        if target_dir is None:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


        if not isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        logs = []
        for filename in listdir(target_dir):
            if filename == '__pycache__':
                continue
           
            full_path_file_name = join(target_dir, filename)
            # stacktrace_log(file)
            filesize = 0
            if isfile(full_path_file_name):
                filesize = getsize(full_path_file_name)

            logs.append(f'- {filename}: file_size={filesize} bytes, is_dir={isdir(full_path_file_name)}')
            

        return " ".join(logs)
    except Exception as e:
        return f'Error: something went wrong: {e}. \n Stacktrace: \n {traceback.format_exc()}'
        


def no_escape(working_dir, directory):
    abs_path_working_dir = abspath(working_dir)
    target_abs_path_dir = abspath(join(working_dir, directory))
    
    if (commonpath([target_abs_path_dir, abs_path_working_dir]) == abs_path_working_dir):
        return target_abs_path_dir
    else:
        return None
    
def clean_path_as_list(path):
    path_arr = path.split('/')
    filtered_path = filter(lambda item: len(item) > 0, path_arr)
    return list(filtered_path)