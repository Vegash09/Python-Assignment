import unittest

from src.namedTuple.util import calculate_average_mark


class TestStudentAverage(unittest.TestCase):

    def test_case_1(self):
        n = 3
        columns = ['ID', 'MARKS', 'NAME', 'CLASS']
        student_data = [
            "1 97 Raymond 7",
            "2 50 Steven 4",
            "3 91 Adrian 9"
        ]
        self.assertEqual(calculate_average_mark(n, columns, student_data), 79.33)