import unittest
import numpy as np

from src.mean_var_std.util import compute_statistics


class TestStatistics(unittest.TestCase):

    def test_case_3x3(self):
        arr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        mean, var, std = compute_statistics(arr)

        np.testing.assert_almost_equal(mean, [2.0, 5.0, 8.0])
        np.testing.assert_almost_equal(var, [6.0, 6.0, 6.0])
        self.assertAlmostEqual(std, 2.58198889747, places=11)

if __name__ == '__main__':
    unittest.main()
