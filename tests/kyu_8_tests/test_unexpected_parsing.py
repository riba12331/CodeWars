import unittest

from katas.kyu_8.unexpected_parsing import get_status


class GetStatusTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_status(True)["status"], "busy")

    def test_equals_2(self):
        self.assertEqual(get_status(False)["status"], "available")
