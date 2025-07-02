import unittest

from src.merge_the_tools.util import merge_the_tools


class TestMergeTheTools(unittest.TestCase):

    def test_case_1(self):
        s = "AABCAAADA"
        k = 3
        expected = ["AB", "CA", "AD"]
        self.assertEqual(merge_the_tools(s, k), expected)