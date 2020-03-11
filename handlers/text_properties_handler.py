from handlers.permission_handler import PermissionHandler

class TextPropertiesWrapper(PermissionHandler):

    """
    Determine global/local text wrappers and other properies.
    Example: color, font-size, etc.
    """

    def __init__(self):
        self.properties = {
            "default_left": 50,
            "default_top": 730,
            "default_line_height": 10,
            "default_font_family": "Arial",
            "default_font_color": "black",
            "default_font_size": 8,

            "left": 0,
            "top": 0,
            "line_height": 0,
            "font_family": 0,
            "font_color": 0,
            "font_size": 0,
        }
        super().__init__(self.parsed)
        super().permissions()

    # Change properties for a selected text section
    # After the changeing set back to the default values
    # So the others won't be affected
    def change_properties(self, object, text, changes):
        print("RUN")
