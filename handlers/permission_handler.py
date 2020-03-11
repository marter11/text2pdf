
class PermissionHandler(object):

    """
    Describe permissions and scope of parsed tokens.
    """

    # DEBUG: with or without control
    def __init__(self, parsed):
        self.__parse = parsed

    def permissions(self):

        for key, value in self.__parse.items():
            value_length = len(value)

            if value_length == 2:
                self.strict_scope(key, value)
            else:
                if key[3] == "~":
                    self.global_scope(key, value)
                else:
                    self.line_scope(key, value)

    # Determine the scope of the <!#x>Text<!#>
    def strict_scope(self, parameter, scope):
        print("Strict", parameter)

    # Determine the scope for the hole line
    def line_scope(self, parameter, scope):
        print("Line", parameter)

    # Determine the global scope and dictates the default properties
    def global_scope(self, raw_parameter, scope):
        process_parameter = raw_parameter.split(" ")
        clean_parameter = process_parameter[0].split("~")[-1]
        clean_value = process_parameter[-1][:-1]

        default = "default_{}".format(clean_parameter)
        self.properties[default] = clean_value

test_dict = {'<!#~font "Arial">': [(0, 15, 0)], '<!#~page_count>': [(0, 13, 1)], '<!#title>': [(0, 8, 3)], '<!#color "red">': [(14, 28, 3), (33, 36, 3)]}
a = PermissionHandler(test_dict)
a.permissions()
