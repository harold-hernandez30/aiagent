
from os import listdir
from os.path import isdir, getsize, isfile, abspath, join, basename
from logger.log import stacktrace_log
import traceback

def print_dir_contents(dir):
    try:
        logs = []
        for file in listdir(dir):
            logs.append(f'- {basename(file)}: file_size={getsize(file)} bytes, is_dir={isdir(file)}')
    except:
        return f'Error: something went wrong'
    
    return " ".join(logs)


def get_files_info(working_directory, directory=None):

    try:

        target_dir = no_escape(working_directory, directory)

        if target_dir is None:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


        if not isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        logs = []
        for file in listdir(target_dir):

            if basename(file) == '__pycache__':
                continue

            filename = basename(file)
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
    
    if (target_abs_path_dir.startswith(abs_path_working_dir)):
        path_arr = clean_path_as_list(target_abs_path_dir)
        target_supposed_working_directory = path_arr[-1]
        if target_supposed_working_directory == working_dir or path_arr[-2] == working_dir:
            return target_abs_path_dir
        else:
            return None
    else:
        return None
    
def clean_path_as_list(path):
    path_arr = path.split('/')
    filtered_path = filter(lambda item: len(item) > 0, path_arr)
    return list(filtered_path)