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
        }
        super().__init__(self.parsed)
        super().permissions()
