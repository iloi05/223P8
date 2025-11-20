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
    
    def test_two_numbers_not_separated_by_commas(self):
        self.assertEqual(self.sc.add("16"), 7)

    def test_two_numbers_separated_by_a_space(self):
        self.assertEqual(self.sc.add("4 3"), 7)

    def test_multiple_numbers_separated_by_commas(self):
        self.assertEqual(self.sc.add("1,2,3,1"), 7)
    
    def test_newline_is_delimiter(self):
        self.assertEqual(self.sc.add("7\n7"), 14)
    
    def test_comma_newline_delimiter(self):
        self.assertEqual(self.sc.add("1\n2,4"), 7)

    def test_single_char_custom_delimiter(self):
        self.assertEqual(self.sc.add("//;\n4;3"), 7)
    
    def test_custom_delimiter_of_multiple_characters(self):
        self.assertEqual(self.sc.add("//[***]\n1***3***3"), 7)

    def test_custom_delimiter_with_special_regex_chars(self):
        self.assertEqual(self.sc.add("//[.*]\n3.*4"), 7)

    def test_digits_in_decimal_seen_as_separate(self):
        self.assertEqual(self.sc.add("1.1,5.9"), 16)

    def test_negative_decimal_numbers_rejected(self):
        with self.assertRaises(ValueError) as context:
            self.sc.add("-1.1,-2.2")
        self.assertIn("-1.1", str(context.exception))
        self.assertIn("-2.2", str(context.exception))

    def test_numbers_past_1000_ignored(self):
        self.assertEqual(self.sc.add("7,7777"), 7)

    def test_1000_not_ignored(self):
        self.assertEqual(self.sc.add("7,1000"), 1007)

    def test_neg_num_exception_raised(self):
        with self.assertRaises(ValueError):
            self.sc.add("-7,-7")

    def test_nonnumeric_vals_ignored(self):
        self.assertEqual(self.sc.add("3,seven,4"), 7)

    def test_skip_empty_tokens(self):
        self.assertEqual(self.sc.add("3,,4"), 7)

    def test_custom_delimiter_without_brackets(self):
        self.assertEqual(self.sc.add("//*\n2*5"), 7)

    def test_multiple_delimiters_inside_brackets(self):
        self.assertEqual(self.sc.add("//[*][%]\n1*1%5"), 7)

    def test_whitespace_ignored(self):
        self.assertEqual(self.sc.add("1, ,6"), 7)

    def test_neg_num_in_custom_delimiter(self):
        with self.assertRaises(ValueError) as context:
            self.sc.add("//;\n1;-1;5")
        self.assertIn("-1", str(context.exception))

    def test_long_multichar_delimiter_mixing_newline(self):
        self.assertEqual(self.sc.add("//[abc]\n1abc2\n4"), 7)


if __name__ == '__main__':
    unittest.main()