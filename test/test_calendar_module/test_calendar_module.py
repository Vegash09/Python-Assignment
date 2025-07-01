import unittest
from src.calendar_module.util import calendar_module


class test_calendar_module(unittest.TestCase):

    def test_calendar(self):
        self.assertEqual(calendar_module("08 05 2015"), "WEDNESDAY")


    def test_calendar2(self):
        self.assertEqual(calendar_module("03 05 2021"), "FRIDAY")

    def test_calendar3(self):
        self.assertEqual(calendar_module("01 01 2019"),"TUESDAY")


if __name__ == '__main__':
    unittest.main()
