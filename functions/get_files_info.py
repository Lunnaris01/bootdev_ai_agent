import os

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

