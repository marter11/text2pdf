from handlers.file_handler import FileHandler, TextFileHandler
import unittest

class FileHandlerTest(unittest.TestCase):
    """
    Test every subroutines which are located in file_handler.py
    """

    def test_read_file(self):
        instance = TextFileHandler()
        

unittest.main()
