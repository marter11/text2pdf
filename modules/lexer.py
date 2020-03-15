
class ParseTokens(object):

    """
    Parse tokens from text.
    """

    # Data argument comes from read_file method, it gives raw text data
    def __init__(self, data):
        self._data = data
        self.parsed = {}

    # Parse data and dump it to an easily readable dict
    def parse(self):

        data = self._data.splitlines()
        cleaned_data = list(data)
        unique_index = 0

        for i in range(0, len(cleaned_data)):
            e = cleaned_data[i]
            e = e.strip()
            iterate = str(e)
            check, difference = 0, 0

            while check > -1:
                start = iterate.find("<!#")
                close = iterate.find(">")
                iterate = iterate[close+1:]
                check = start

                if check > -1:
                    item = e[start+difference:close+difference+1]
                    if item == "<!#>":
                        self.parsed[unique_index-1][-1].append((start+difference, close+difference, i))
                    else:

                        # (start_tag, close_tag, line_index)
                        self.parsed[unique_index] = [item, [(start+difference, close+difference, i)]]
                        unique_index += 1


                    # Set cleaned tex data (without parameters)
                    cleaned_data[i] = cleaned_data[i].replace(item, "")

                difference = difference+close+1

        # DEBUG:
        # How to give font and color to the same part of text
        return (cleaned_data, data)
