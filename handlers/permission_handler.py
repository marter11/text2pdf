from modules import split_text_to_scope

class PermissionHandler(object):

    """
    Describe permissions and scope of parsed tokens.
    """

    # DEBUG: with out withot controll
    def permissions(self):

        for index, value in self.parsed.items():
            value_length = len(value[-1])
            self.__determine_line = index

            key = self.parsed[index][0]

            if value_length == 2:
                self.strict_scope(key, value)
            else:

                if key[3] == "~":
                    self.global_scope(key, value)
                else:
                    self.line_scope(key, value)

    # Common parameters for line and for strict also
    def common_scope_parameters(self, parameter, type):

        values = parameter.split(" ")

        if len(values) == 2:
            key = values[0][3:]
            value = values[1][:-1]

            # If exists for example: <!#font_color><!#title>
            # Store the same lined inline
            if len(self.apply) > 0:
                current_full = self.parsed[self.__determine_line]
                self_apply_contains_check_index = current_full[-1][-1][-1]
                contains = self.apply.get(self_apply_contains_check_index)

                if contains:
                    data = contains.get(type)
                    self.apply[self_apply_contains_check_index][type][key] = value

                else:
                    pass

            elif len(self.apply) == 0:
                self.apply[self.__determine_line] = {type: {key: value}}

    # Determine the scope of the <!#x>Text<!#>
    def strict_scope(self, parameter, scope):
        pass

    # Determine the scope for the hole line
    def line_scope(self, parameter, scope):

        # Special line scope parameters
        if parameter == "<!#title>":
            self.apply[self.__determine_line] = {"line": {"left": 250}}
        else:
            self.common_scope_parameters(parameter, "line")

    # Determine the global scope and dictates the default properties
    def global_scope(self, raw_parameter, scope):
        process_parameter = raw_parameter.split(" ")
        clean_parameter = process_parameter[0].split("~")[-1]
        clean_value = process_parameter[-1][:-1]

        default = "default_{}".format(clean_parameter)
        self.properties[default] = clean_value

# test_dict = {'<!#~font "Arial">': [(0, 15, 0)], '<!#~page_count>': [(0, 13, 1)], '<!#title>': [(0, 8, 3)], '<!#color "red">': [(14, 28, 3), (33, 36, 3)]}
# a = PermissionHandler(test_dict)
# a.permissions()
