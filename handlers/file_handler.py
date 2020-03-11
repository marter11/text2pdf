from handlers.text_object_handler import PDFHandler
from modules import ParseTokens

class TextFileHandler(object):

    """
    Reads txt file and obtain information about it.
    """

    # Reads the data contained by text file
    def read_file(self):
        file = open(self._src, "r")
        data = file.read()
        file.close()
        return data

class FileHandler(TextFileHandler, PDFHandler):

    """
    Connects methods what are related to file processing.
    """

    def __init__(self, destination, source, name):
        self._dest = destination
        self._src = source
        self.name = name

    def setup_pdf_processing(self, raw_text):
        object = ParseTokens(raw_text)
        self.cleaned_data = object.parse()
        self.parsed = object.parsed

        return self
