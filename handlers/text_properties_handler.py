from handlers.permission_handler import PermissionHandler
from modules import split_text_to_scope

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

            "left": None,
            "top": None,
            "line_height": None,
            "font_family": None,
            "font_color": None,
            "font_size": None,
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

                self.properties["font_color"] = font_color

                object.setTextOrigin(int(left), int(top))
                object.setFillColor(font_color)
                object.setFont(font_family, int(font_size))

            # Set properties only to specific scope
            if strict:
                self.text_out = False

                current_line_clean_text = self.cleaned_data[current_line]
                save_properties_state = self.properties
                separated_shift_difference = 0
                l = len(strict)
                c = 0

                for key, value in strict.items():
                    font_color, scope = value.get("font_color", self.properties["default_font_color"])
                    separated_segments, separated_shift_difference, affected_item_index = split_text_to_scope(scope, current_line_clean_text, separated_shift_difference)

                    if c < l-1:
                        to = -1
                    else:
                        to = len(separated_segments)

                    # Handle separetly the affected items and the non-affected ones
                    iterate_over = len(separated_segments[:to])
                    for item_index in range(iterate_over):

                        if item_index == affected_item_index:
                            font_color = value.get("font_color", ["black"])[0]
                            # top = line.get("top", self.properties["default_top"]-(int(self.properties["default_line_height"])*down_by_current_line))
                            # left = line.get("left", self.properties["default_left"])
                            object.setFillColor(font_color)
                            object.textOut(separated_segments[item_index])

                        else:
                            font_color = self.properties.get("font_color", self.properties["default_font_color"])
                            object.setFillColor(font_color)
                            object.textOut(separated_segments[item_index])

                        self.properies = save_properties_state

                    current_line_clean_text = separated_segments[-1]
                    c += 1

        return object
