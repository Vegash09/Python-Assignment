import unittest

from src.find_the_runner.util import second_highest_number


class TestSecondHighestNumber(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(second_highest_number([1, 2, 3, 4, 5]), 4)

    def test_with_duplicates(self):
        self.assertEqual(second_highest_number([10, 20, 20, 30]), 20)


if __name__ == '__main__':
    unittest.main()
