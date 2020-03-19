from handlers import FileHandler, PDFHandler
from modules import ParseTokens
import sys
import os

# If want to convert file directly to pdf (run as script)
if __name__ == "__main__":

    l = len(sys.argv)
    if l == 2:
        src = sys.argv[1]
        dest = os.getcwd()
        name = src.split("/")[-1]

    elif l >= 3:
        src, dest = sys.argv[1], sys.argv[2]

        try:
            os.chdir(dest)
        except:
            split = dest.split("/")
            name = split[-1]
            split.pop(-1)
            os.chdir("/".join(split))
        else:
            name = src.split("/")[-1]

    else:
        raise TypeError("Invalid or no parameters!")

    file_handler = FileHandler(dest, src, name)
    raw_text = file_handler.read_file()
    file_handler.setup_pdf_processing(raw_text)
    file_handler.write_pdf()
