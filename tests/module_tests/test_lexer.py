from modules.lexer import ParseTokens
import unittest

class TestLexer(unittest.TestCase):

    """
    Test lexer token parsing and processes.
    """
    
    def setUp(self):
        with open("tests/module_tests/testable_texts/lexer.txt", "r") as f:
            data = f.read()

        self.object = ParseTokens(data)

    def test_parser_return(self):
        return_data = self.object.parse()
        raw = [
                "<!#~font_color red>", "<!#~font_size 50>", "",
                "", "<!#title>This is the title section", "",
                "Clean field here without loerm ipsum",
                "<!#font_color blue>And this is <!#font_color green>also a cool thing<!#> so yeah.",
                "<!#font_size 50> To the full text",
                "End of the text file."
                ]
        cleaned = [
                    "", "", "This is the title section", "",
                    "Clean field here without loerm ipsum",
                    "And this is also a cool thing so yeah.",
                    " To the full text",
                    "End of the text file."
                    ]

        self.assertEqual(len(return_data), 2)
        self.assertEqual(return_data[0], cleaned)
        self.assertEqual(return_data[1], raw)

    def test_parsed_dict(self):
        self.object.parse()
        parsed = self.object.parsed

        self.assertEqual(len(parsed), 6)
        self.assertEqual(parsed[0], ["<!#~font_color red>", [(0, 18, 0)]])
        self.assertEqual(parsed[4], ["<!#font_color green>", [(12, 31, 7), (29, 32, 7)]])

    def test_parsed_dict_structure(self):
        self.object.parse()
        parsed = self.object.parsed

        for key, value in parsed.items():
            self.assertEqual(type(key).__name__, "int")
            self.assertEqual(len(value), 2)
            self.assertGreaterEqual(len(value[1]), 1)
