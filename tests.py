import unittest
from functions.run_python import run_python_file

class TestRunPythonFile(unittest.TestCase):

    def test_run_main(self):
        result = run_python_file("calculator", "main.py")
        expected = 'Calculator App'
        self.assertTrue(expected in result)
        print(result)

    def test_run_tests(self):
        result = run_python_file("calculator", "tests.py")
        expected = 'Ran'
        self.assertTrue(expected in result)
        print(result)

    
    def test_run_outside_working_dir(self):
        result = run_python_file("calculator", "../main.py")
        expected = 'Error: Cannot execute "../main.py" as it is outside the permitted working directory'
        self.assertEqual(result, expected)
        print(result)

    def test_run_non_existent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        expected = 'Error: File "nonexistent.py" not found.' 
        self.assertEqual(result, expected)
        print(result)

if __name__ == '__main__':
    unittest.main()