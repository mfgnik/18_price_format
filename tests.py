import unittest
from format_price import format_price


class Test_format_price(unittest.TestCase):
    def test_integer_number(self):
        self.assertEqual(format_price('23112.000'), '23 112')

    def test_value_error(self):
        self.assertIsNone(format_price('eq221'))

    def test_fractional_number_without_round(self):
        self.assertEqual(format_price('4.364'), '4.36')

    def test_fractional_number_with_round(self):
        self.assertEqual(format_price('4.365'), '4.37')


if __name__ == '__main__':
    unittest.main()
