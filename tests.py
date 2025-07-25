# tests.py

import unittest
from functions.get_files_info import get_files_info, get_file_content, SCHEMA_GET_FILES_INFO
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestCalculator(unittest.TestCase): 
	
	
#	def test_pwd(self):
#		result = get_files_info("calculator", ".")
#		print(result)
#	def test_pkg(self):
 #       	result = get_files_info("calculator", "pkg")
  #      	print(result)
#	def test_rootfolder(self):
#		result = get_files_info("calculator","/bin")
#		print(result)
#	def test_parentfolder(self):
#		result = get_files_info("calculator","../")
#		print(result)
#	def test_lorem(self):
#		result = get_file_content("calculator","lorem.txt")
#		print(result)
#	def test_main(self):
#		result = get_file_content("calculator", "main.py")
#		print(result)
#	def test_calc_pkg(self):
#		result = get_file_content("calculator", "pkg/calculator.py")
#		print(result)
#	def test_nonworkingdir(self):
#		result = get_file_content("calculator", "/bin/cat")
#		print(result)
	def test_writefile(self):
		result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
		print(result)
	def test_writeorderfile(self):
		result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
		print(result)
	def test_writeillegal(self):
		result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
		print(result)
	def testrunner_1(self):
		result = run_python_file("calculator", "main.py") 
		print(result)
	def testrunner_2(self):
		result = run_python_file("calculator", "main.py", ["3 + 5"])
		print(result)

	def testrunner_3(self):
		result = run_python_file("calculator", "tests.py")
		print(result)


	def testrunner_4(self):
		result = run_python_file("calculator", "../main.py")
		print(result)

	def testrunner_5(self):
		result = run_python_file("calculator", "nonexistent.py")
		print(result)

if __name__ == "__main__":
    unittest.main()
