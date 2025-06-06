from functions.get_file_content import get_file_content
import unittest

class TestGetFileContent(unittest.TestCase):

    def test_working_directory_read(self):
        content = get_file_content("calculator", "main.py")
        self.assertTrue("def main()" in content)
        print(content)

    def test_subdirectory_read(self):
        content = get_file_content("calculator", "pkg/calculator.py")
        self.assertTrue("def evaluate(self, expression):" in content)
        print(content)

    def test_exceed_non_max_length(self):
        self.assertEqual(get_file_content("calculator", "/bin/cat"), 'Error: "/bin/cat" tried to escape')

if __name__ == '__main__':
    unittest.main()