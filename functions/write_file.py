import os

def write_file(working_directory, file_path, content):
        abs_working_dir = os.path.abspath(working_directory)
        abs_filepath = os.path.abspath(os.path.join(abs_working_dir,file_path))
        if not abs_filepath.startswith(abs_working_dir):
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
        if not os.path.exists(abs_filepath):
                os.makedirs(os.path.dirname(abs_filepath), exist_ok=True)
        with open(abs_filepath,"w") as file:
                file.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
