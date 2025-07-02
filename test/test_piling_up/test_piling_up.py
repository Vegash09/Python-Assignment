import unittest

from src.piling_up.util import can_stack_blocks


class TestPilingUp(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(can_stack_blocks([4, 3, 2, 1, 3, 4]), "Yes")