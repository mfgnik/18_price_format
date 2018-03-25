import unittest
from format_price import format_price


class Test_format_price(unittest.TestCase):
    def test_integer_number_bigger_thousand(self):
        self.assertEqual(format_price('23112.000'), '23 112')

    def test_integer_number_less_thousand(self):
        self.assertEqual(format_price('23.000'), '23')

    def test_value_error(self):
        self.assertIsNone(format_price('eq221'))

    def test_fractional_number_without_round(self):
        self.assertEqual(format_price('4.364'), '4.36')

    def test_fractional_number_with_round(self):
        self.assertEqual(format_price('4.365'), '4.37')

    def test_no_value(self):
        self.assertIsNone(format_price(''))

    def test_nothing_after_point(self):
        self.assertEqual(format_price('5.'), '5')

    def test_nothing_before_point(self):
        self.assertEqual(format_price('0.543'), '0.54')

    def test_no_point(self):
        self.assertEqual(format_price('5'), '5')


if __name__ == '__main__':
    unittest.main()
