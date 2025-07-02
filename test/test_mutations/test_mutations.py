import unittest

from src.mutations.util import mutate_string


class TestMutateString(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")