from functions.escape_check import validate_escape
from os.path import exists, splitext, abspath
import subprocess

def run_python_file(working_directory, file_path):
    
    target_abs_file_path = validate_escape(working_directory, file_path)

    if target_abs_file_path is None:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not exists(target_abs_file_path):
        return f'Error: File "{file_path}" not found.'
    

    filename, extension = splitext(file_path)


    if extension != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    proc = subprocess.run(["python3", file_path], timeout=30, capture_output=True, cwd=abspath(working_directory))
    return proc_result_output(proc)
    


def proc_result_output(proc):
    results = []
    results.append(f'STDOUT: {proc.stdout}')
    results.append(f'STDERR: {proc.stderr}')
    
    if (proc.returncode != 0):
        results.append(f'Error: Process excited with code {proc.returncode}')

    return ", ".join(results)