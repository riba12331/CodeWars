import unittest

from kyu_8.number_to_string import number_to_string


class NumberToStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(number_to_string(67), '67')


if __name__ == '__main__':
    unittest.main()