from functions.get_file_content import get_file_content
import unittest

class TestGetFileContent(unittest.TestCase):

    def test_exceed_max_length(self):
        MAX_LENGTH = 10000
        appended_length = len('[...File "lorem.txt" truncated at 10000 characters]')
        self.assertEqual(len(get_file_content('lorem', 'lorem.txt')), MAX_LENGTH + appended_length)

    def test_exceed_non_max_length(self):
        self.assertEqual(len(get_file_content('lorem', 'lorem_5k.txt')), 5000)

if __name__ == '__main__':
    unittest.main()