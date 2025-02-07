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

            self.text_out = True

            # Add page loadness (if bigger than x start new page)
            newline_top = int(properties["default_top"])-(int(properties["default_line_height"])*down_by_current_line)

            # Open new page if neccessary
            new_page = False
            current_line_check = self.apply.get(current_line)
            if current_line_check:
                line_check = current_line_check.get("line")
                if line_check:
                    new_page = line_check.get("new_page")

            if newline_top < 100 or new_page:
                handler.showPage()
                self.textObject = handler.beginText()
                self.properties["default_top"] = 800
                down_by_current_line = 0
                newline_top = int(properties["default_top"])-(int(properties["default_line_height"])*down_by_current_line)

            # This rack of code sets to default after every change
            if current_line not in self.filtered_white_global_lines:
                self.textObject.setTextOrigin(int(properties["default_left"]), newline_top)
                self.textObject.setFillColor(self.properties["default_font_color"])
                self.textObject.setFont(self.properties["default_font_family"], int(self.properties["default_font_size"]))

                self.textObject = self.change_properties(self.textObject, current_line, down_by_current_line)

                if self.text_out:
                    self.textObject.textOut(self.cleaned_data[current_line])
                else:
                    pass

                handler.drawText(self.textObject)
                down_by_current_line += 1

            current_line += 1


        handler.save()
