
class ParseTokens(object):

    """
    Parse tokens from text.
    """

    # Data argument comes from read_file method, it gives raw text data
    def __init__(self, data):
        self._data = data
        self.parsed = {}
        self.filter_white_global_lines = []

    # Parse data and dump it to an easily readable dict
    def parse(self):

        data = self._data.splitlines()
        cleaned_data = list(data)
        act_dat = list(data)
        unique_index = 0
        filter_white_global_lines = []

        for i in range(0, len(cleaned_data)):
            e = cleaned_data[i]
            text_segment_without_parameters_parse = [x for x in cleaned_data[i]]
            check, difference = 0, 0

            while check > -1:
                iterate = "".join(text_segment_without_parameters_parse)
                start = iterate.find("<!#")
                close = iterate.find(">")
                check = start

                if check > -1:
                    item = iterate[start:close+1]

                    if item == "<!#>":
                        self.parsed[unique_index-1][-1].append((start, close, i))

                    else:

                        # (start_tag, close_tag, line_index)
                        self.parsed[unique_index] = [item, [(start, close, i)]]

                    text_segment_without_parameters_parse[start:close+1] = ""
                    replaced_part = "".join(text_segment_without_parameters_parse)

                    if replaced_part == "":
                        filter_white_global_lines.append(i)

                    cleaned_data[i] = "".join(text_segment_without_parameters_parse)
                    unique_index += 1

        self.filter_white_global_lines = filter_white_global_lines

        # DEBUG:
        # How to give font and color to the same part of text
        # Idea, just use <!#parameter1 value1, parameter2 value2>

        return (cleaned_data, data)
