from functions.get_files_info import get_files_info
import unittest

class TestGetFilesInfo(unittest.TestCase):

    def test_current_dir(self):
        self.assertAndPrint(get_files_info('calculator', '.'), "- main.py: file_size=575 bytes, is_dir=False - tests.py: file_size=1342 bytes, is_dir=False - pkg: file_size=0 bytes, is_dir=True")

    def test_pkg(self):
        self.assertAndPrint(get_files_info('calculator', 'pkg'), "- calculator.py: file_size=1737 bytes, is_dir=False - render.py: file_size=766 bytes, is_dir=False")

    
    def test_root_access(self):
        self.assertAndPrint(get_files_info('calculator', '/bin'), 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    
    def test_outside_access(self):
        self.assertAndPrint(get_files_info('calculator', '../'), 'Error: Cannot list "../" as it is outside the permitted working directory')

    
    def test_not_a_dir(self):
        self.assertAndPrint(get_files_info('calculator', 'main.py'), 'Error: "main.py" is not a directory')


    def assertAndPrint(self, result, expected):
        print(result)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()