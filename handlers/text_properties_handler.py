from handlers.permission_handler import PermissionHandler

class TextPropertiesWrapper(PermissionHandler):

    """
    Determine global/local text wrappers and other properies.
    Example: color, font-size, etc.
    """

    def __init__(self):
        self.properties = {
            "default_left": 50,
            "default_top": 800,
            "default_line_height": 10,
            "default_font_family": "Times-Roman",
            "default_font_color": "black",
            "default_font_size": 10,

            "left": 0,
            "top": 0,
            "line_height": 0,
            "font_family": 0,
            "font_color": 0,
            "font_size": 0,
        }

        self.apply = {}

        super().permissions()

    # Change properties for a selected text section
    # After the changeing set back to the default values
    # So the others won't be affected
    def change_properties(self, object, current_line, down_by_current_line):
        current_appliable = self.apply.get(current_line)

        if current_appliable:
            line = current_appliable.get("line")
            strict = current_appliable.get("strict")

            # Set properties to the full line
            if line:
                left = line.get("left", self.properties["default_left"])
                top = line.get("top", self.properties["default_top"]-(int(self.properties["default_line_height"])*down_by_current_line))
                font_color = line.get("font_color", self.properties["default_font_color"])
                font_size = line.get("font_size", self.properties["default_font_size"])
                font_family = line.get("font_family", self.properties["default_font_family"])

                object.setTextOrigin(int(left), int(top))
                object.setFillColor(font_color)
                object.setFont(font_family, int(font_size))

            # Set properties only to specific scope
            # Important! Strict specified only accepts non cleaned_data because it compares
            # to <!#parameter> values also, lexer doesen't remove them while count it
            if strict:
                current_line_text = self.data[current_line]
                current_line_clean_text = self.cleaned_data[current_line]

                for key, value in strict.items():
                    count_from = 0

                    font_color, scope = value.get("font_color", self.properties["default_font_color"])
                    print(scope)

        return object
