import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.sc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.sc.add(""), 0)
    
    def test_single_number_returns_itself(self):
        self.assertEqual(self.sc.add("7"), 7)
    
    def test_two_numbers_separated_by_commas(self):
        self.assertEqual(self.sc.add("7,7"), 14)
    
    def test_multiple_numbers_separated_by_commas(self):
        self.assertEqual(self.sc.add("1,2,3,1"), 7)
    
    def test_newline_is_delimiter(self):
        self.assertEqual(self.sc.add("7\n7"), 14)
    
    def test_comma_newline_mixed_delimiters(self):
        self.assertEqual(self.sc.add("1\n2,4"), 7)

    def test_single_char_custom_delimiter(self):
        self.assertEqual(self.sc.add("//;\n4;3"), 7)
    
    def test_custom_delimiter_of_multiple_characters(self):
        self.assertEqual(self.sc.add("//[***]\n1***3***3"), 7)

    def test_custom_delimiter_with_special_regex_chars(self):
        self.assertEqual(self.sc.add("//[.*]\n3.*4"), 7)

    def test_numbers_past_1000_ignored(self):
        self.assertEqual(self.sc.add("7,7777"), 7)


if __name__ == '__main__':
    unittest.main()