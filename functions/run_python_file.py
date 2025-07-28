import os
import subprocess 
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
	name="run_python_file",
	description="Run a .py file with the python interpreter if it is located within the allowed working directory",
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			"file_path": types.Schema(
				type=types.Type.STRING,
				description="path and filename, relative to the working directory. This parameter is required.",
			),
                        "args": types.Schema(
                                type=types.Type.ARRAY,
                                description="A list of command-line arguments.",
                                items=types.Schema(
                                        type=types.Type.STRING,
                                        description="A single argument."
                                )
                        ),
		},
	),
)



def run_python_file(working_directory, file_path, args=[]):
        abs_working_dir = os.path.abspath(working_directory)
        abs_filepath = os.path.abspath(os.path.join(abs_working_dir,file_path))
        if not abs_filepath.startswith(abs_working_dir):
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        print(abs_filepath)
        print(os.path.isfile(abs_filepath))
        if not os.path.isfile(abs_filepath):
                return f'Error: File "{file_path}" not found.'
        if not abs_filepath[-3:] == '.py':
                return f'Error: "{file_path}" is not a Python file.'
        try:
            completed_process = subprocess.run( ["python" , abs_filepath ] + args, capture_output=True, timeout=30)
        except Exception as e:
                return f"Error: executing Python file: {e}"
        ret_str = ""
        if completed_process.returncode == 0:
                ret_str += "Function finished successfully (Return Code 0)\n"
        else:
                ret_str += f"Function failed (Return Code: {completed_process.returncode}) \n"
        if completed_process.stdout == "":
                 "No output on STDOUT produced\n"
        else:
                ret_str += f'STDOUT: {completed_process.stdout}\n'

        if completed_process.stderr != "":
                ret_str += f'STDERR: {completed_process.stderr}'
        return ret_str        




