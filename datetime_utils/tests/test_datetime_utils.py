import unittest
from datetime import datetime
from datetime_utils import add_days, days_between

class TestDateTimeUtils(unittest.TestCase):
    def test_add_days(self):
        self.assertEqual(add_days(datetime(2023, 1, 1), 5), datetime(2023, 1, 6))
        self.assertEqual(add_days(datetime(2023, 1, 1), -5), datetime(2022, 12, 27))

    def test_days_between(self):
        self.assertEqual(days_between(datetime(2023, 1, 1), datetime(2023, 1, 6)), 5)
        self.assertEqual(days_between(datetime(2023, 1, 1), datetime(2022, 12, 27)), -5)

if __name__ == "__main__":
    unittest.main()
