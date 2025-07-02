import unittest

from src.iterables_iterators.util import probability_with_a


class TestProbabilityWithA(unittest.TestCase):

    def test_case_1(self):
        lst = ['a', 'b', 'c', 'd']
        pick = 2
        self.assertEqual(probability_with_a(lst, pick), 0.5)

    def test_case_2(self):
        lst = ['a', 'a', 'a', 'a']
        pick = 2
        self.assertEqual(probability_with_a(lst, pick), 1.0)