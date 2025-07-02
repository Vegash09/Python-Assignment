import unittest

from src.delta_time.util import time_delta


class TestTimeDelta(unittest.TestCase):

    def test_case_1(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "25200")  # 7 hours = 25200 seconds


if __name__ == "__main__":
    unittest.main()
