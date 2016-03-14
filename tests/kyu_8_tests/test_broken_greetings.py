import unittest

from kyu_8.broken_greetings import Person


class PersonTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Person('Z').greet('Jim'), 'Hi Jim, my name is Z')


if __name__ == '__main__':
    unittest.main()