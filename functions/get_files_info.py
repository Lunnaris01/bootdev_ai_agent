import os
from google.genai import types


MAX_CHARS = 10000
SCHEMA_GET_FILES_INFO = types.FunctionDeclaration(
	name="get_files_info",
	description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			"directory": types.Schema(
				type=types.Type.STRING,
				description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
			),
		},
	),
)




def get_files_info(working_directory, directory=None):
	abs_working_dir = os.path.abspath(working_directory)
	abs_path = os.path.abspath(os.path.join(abs_working_dir,directory))
	#print(abs_path)
	#print(abs_working_dir)
	if not abs_path.startswith(abs_working_dir):
		return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
	contents = [f"- {filename}: file_size={os.path.getsize(os.path.join(abs_path,filename))}, is_dir={not os.path.isfile(os.path.join(abs_path,filename))}" for filename in os.listdir(abs_path)]
	ret_str = f"Results for '{directory}' directory:\n" + "\n".join(contents)
	print(ret_str)
get_files_info("calculator","pkg")	


def get_file_content(working_directory, file_path):
	abs_working_dir = os.path.abspath(working_directory)
	abs_filepath = os.path.abspath(os.path.join(abs_working_dir,file_path))
	if not abs_filepath.startswith(abs_working_dir):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	if not os.path.isfile(abs_filepath):
		return f'Error: File not found or is not a regular file: "{file_path}"'
	with open(abs_filepath) as file:
		content = file.read()
		if len(content) > MAX_CHARS:
			return content[:10000] + f'[... File \"{file_path}\" truncated at 10000 characters]'
		return content



