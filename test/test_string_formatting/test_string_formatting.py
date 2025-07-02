import unittest

from src.string_formatting.util import print_formatted


class TestFormattedPrint(unittest.TestCase):

    def test_case_1(self):
        expected = [
            '  1   1   1   1',
            '  2   2   2  10',
            '  3   3   3  11',
            '  4   4   4 100',
            '  5   5   5 101'
        ]
        self.assertEqual(print_formatted(5), expected)

