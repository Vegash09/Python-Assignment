import unittest

from src.finding_the_percentage.util import finding_the_percentage


class TestFindingThePercentage(unittest.TestCase):

    def test_valid_student(self):
        data = [
            ('Krishna', [67, 68, 69]),
            ('Arjun', [70, 98, 63]),
            ('Malika', [52, 56, 60])
        ]
        self.assertEqual(finding_the_percentage(data, 'Malika'), 56.00)



if __name__ == '__main__':
    unittest.main()
