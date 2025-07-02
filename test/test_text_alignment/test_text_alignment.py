import unittest

from src.text_alignment.util import generate_logo


class TestLogo(unittest.TestCase):

    def test_basic_thickness(self):
        output = generate_logo(2, 'H')
        self.assertEqual(len(output), 11)