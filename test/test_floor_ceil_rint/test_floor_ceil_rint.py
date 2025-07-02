import numpy as np
import unittest

from src.floor_ceil_rint.util import process_array


class TestArrayRounding(unittest.TestCase):

    def test_mixed_values(self):
        input_str = "1.1 -2.5 3.9 -4.2"
        expected_floor = np.array([1., -3., 3., -5.])
        expected_ceil = np.array([2., -2., 4., -4.])
        expected_rint = np.array([1., -2., 4., -4.])
        floor, ceil, rint = process_array(input_str)
        np.testing.assert_array_equal(floor, expected_floor)
        np.testing.assert_array_equal(ceil, expected_ceil)
        np.testing.assert_array_equal(rint, expected_rint)