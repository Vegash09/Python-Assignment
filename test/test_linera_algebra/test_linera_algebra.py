import unittest

from src.linera_algebra.util import calculate_determinant


class TestDeterminant(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(calculate_determinant(matrix), -2.0)