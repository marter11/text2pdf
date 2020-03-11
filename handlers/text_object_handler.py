from reportlab.pdfgen import canvas
from handlers.text_properties_handler import TextPropertiesWrapper

class PDFHandler(TextPropertiesWrapper):

    """
    Converts cleaned text data to pdf format.
    """

    def __init__(self, cleaned_data, parsed_tokens):
        self._data = cleaned_data
        self.__parsed_tokens = parsed_tokens

    def write_pdf(self):

        # Necessary values
        super().__init__()
        lines_length = len(self.cleaned_data)
        current_line = 0
        properties = self.properties

        print("Test:", self.properties["default_left"], self.properties["default_font_size"])

        file_name = "".join(self.name.split(".")[:-1])+".pdf"
        handler = canvas.Canvas(file_name)

        # If using without control use the same subroutine just split the text
        # After line break l.setTextOrigin(50, pervious-line_height)

        while lines_length > current_line:
            textObject = handler.beginText()

            # Change properties["xy"] to line_scope and strict_scope friendly
            textObject.setTextOrigin(int(properties["default_left"]), int(properties["default_top"])-(int(properties["default_line_height"])*current_line))
            textObject.textOut(self.cleaned_data[current_line])

            handler.drawText(textObject)
            current_line += 1

        handler.save()
        # l.setTextOrigin(50, 730)
        # l.textOut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # l.setTextOrigin(50, 720)
        # l.textOut("ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC")
        # l.setTextOrigin(50, 710)
        # l.textOut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # handler.drawText(l)
        # handler.save()
