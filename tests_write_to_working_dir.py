import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):

    def test_write_to_working_dir(self):
        file = "lorem.txt"
        result = write_file("target", file, "wait, this isn't lorem ipsum")
        expected_length = len("wait, this isn't lorem ipsum")
        expected = f'Successfully wrote to "{file}" ({expected_length} characters written)'
        self.assertEqual(result, expected)
        print(expected)

    def test_write_to_working_dir_subdirectory(self):
        file = "pkg/morelorem.txt"
        result = write_file("target", file, "lorem ipsum dolor sit amet")
        expected_length = len("lorem ipsum dolor sit amet")
        expected = f'Successfully wrote to "{file}" ({expected_length} characters written)'
        self.assertEqual(result, expected)
        print(expected)

    
    def test_write_to_outside_working_dir(self):
        file = "/tmp/temp.txt"
        result = write_file("target", file, "this should not be allowed")
        expected = f'Error: Cannot write to "{file}" as it is outside the permitted working directory'
        self.assertEqual(result, expected)
        print(expected)

if __name__ == '__main__':
    unittest.main()