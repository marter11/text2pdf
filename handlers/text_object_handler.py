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

        file_name = "".join(self.name.split(".")[:-1])+".pdf"
        handler = canvas.Canvas(file_name)
        self.textObject = handler.beginText()
        super().__init__()
        lines_length = len(self.cleaned_data)
        current_line = 0
        properties = self.properties
        down_by_current_line = 0

        # If using without control use the same subroutine just split the text
        # After line break l.setTextOrigin(50, pervious-line_height)

        while lines_length > current_line:

            # Add page loadness (if bigger than x start new page)
            # On new page create new handler.beginText()

            # DEBUG: current line is left over by n+1 and the n+1 line's parameter affect the n-th line
            # especially when define global parameters
            newline_top = int(properties["default_top"])-(int(properties["default_line_height"])*down_by_current_line)

            if newline_top < 100:
                # handler.drawText(self.textObject)
                handler.showPage()
                self.textObject = handler.beginText()
                self.properties["default_top"] = 800
                down_by_current_line = 0
                newline_top = int(properties["default_top"])-(int(properties["default_line_height"])*down_by_current_line)

            # This rack of code sets to default after every change
            self.textObject.setTextOrigin(int(properties["default_left"]), newline_top)
            self.textObject.setFillColor(self.properties["default_font_color"])
            self.textObject.setFont(self.properties["default_font_family"], int(self.properties["default_font_size"]))

            self.textObject = self.change_properties(self.textObject, current_line, down_by_current_line)
            self.textObject.textOut(self.cleaned_data[current_line])
            handler.drawText(self.textObject)

            current_line += 1
            down_by_current_line += 1

        print(self.apply)
        handler.save()
