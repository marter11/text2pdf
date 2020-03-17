from handlers.file_handler import FileHandler, TextFileHandler
import unittest

class FileHandlerTest(unittest.TestCase):

    """
    Test boilerplateing for pdf processes.
    """

    def setUp(self):
        self.destination = "tests/module_tests/testable_texts"
        self.source = "tests/module_tests/testable_texts/lexer.txt"
        self.name = "lexer.pdf"

        with open(self.source, "r") as f:
            self.text = f.read()

        self.object = FileHandler(self.destination, self.source, self.name)

    def test_handler_init(self):
        self.assertEqual(self.object._dest, self.destination)
        self.assertEqual(self.object._src, self.source)
        self.assertEqual(self.object.name, self.name)

    def test_pdf_process_boilerplateing(self):
        self.object.setup_pdf_processing(self.text)
        self.assertGreater(len(self.object.parsed), 0)
        self.assertGreater(len(self.object.cleaned_data), 0)
        self.assertGreater(len(self.object.data), 0)

class TextFileHandlerTest(unittest.TestCase):

    def setUp(self):
        self.source = "tests/module_tests/testable_texts/lexer.txt"

        with open(self.source, "r") as f:
            self.text = f.read()

    def test_output_data(self):
        object = TextFileHandler()
        object._src = self.source
        self.assertEqual(object.read_file(), self.text)
