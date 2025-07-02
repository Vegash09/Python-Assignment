import unittest

from src.no_idea.util import calculate_happiness


class TestHappiness(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        self.assertEqual(calculate_happiness(arr, A, B), 1)