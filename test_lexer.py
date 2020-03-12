from modules.lexer import ParseTokens
import unittest

class TestLexer(unittest.TestCase):

    def setUp(self):
        with open("t.txt", "r") as f:
            data = f.read()
        self.object = ParseTokens(data)

    def test_parse_return(self):
        return_data = self.object.parse()
        self.assertEqual(type(return_data).__name__, "list")

        found_count = 0
        for e in return_data:
            if e.find("<!#") != -1:
                found_count += 1

        self.assertEqual(found_count, 0)

    def test_for_hidden_parsed_dict(self):
        object = self.object
        object.parse()
        parsed_length = len(object.parsed)
        self.assertEqual(parsed_length, 8)

unittest.main()
