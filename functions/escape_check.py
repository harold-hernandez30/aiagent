from os import listdir
from os.path import abspath, join, commonpath

def validate_escape(working_directory, file):
    if file is None:
        return working_directory

    abs_path_working_dir = abspath(working_directory)
    abs_path_target_file = abspath(join(working_directory, file))
    common_path = commonpath([abs_path_working_dir, abs_path_target_file])
    if common_path == abs_path_working_dir:
        return abs_path_target_file
    
    return None