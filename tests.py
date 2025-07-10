# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase): 
	
	
	def test_pwd(self):
		result = get_files_info("calculator", ".")
		print(result)
	def test_pkg(self):
        	result = get_files_info("calculator", "pkg")
        	print(result)
	def test_rootfolder(self):
		result = get_files_info("calculator","/bin")
		print(result)
	def test_parentfolder(self):
		result = get_files_info("calculator","../")
		print(result)
if __name__ == "__main__":
    unittest.main()
