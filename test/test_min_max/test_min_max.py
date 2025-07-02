import unittest

from src.min_max.util import max_of_row_mins


class TestMaxOfRowMins(unittest.TestCase):

    def test_case_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(max_of_row_mins(matrix), 7)