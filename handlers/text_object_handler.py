from handlers.text_properties_handler import TextPropertiesWrapper
from reportlab.pdfgen import canvas

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

        file_name = "".join(self.name.split(".")[:-1])+".pdf"
        handler = canvas.Canvas(file_name)

        # If using without control use the same subroutine just split the text
        # After line break l.setTextOrigin(50, pervious-line_height)


        self.textObject = handler.beginText()
        while lines_length > current_line:
            # Add page loadness (if bigger than x start new page)

            # Change properties["xy"] to line_scope and strict_scope friendly
            self.textObject.setTextOrigin(int(properties["default_left"]), int(properties["default_top"])-(int(properties["default_line_height"])*current_line))

            self.textObject.textOut(self.cleaned_data[current_line])
            # self.strict_scope("fafa", 3)
            handler.drawText(self.textObject)

            current_line += 1

        handler.save()
