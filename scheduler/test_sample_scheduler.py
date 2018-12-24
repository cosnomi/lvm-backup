import unittest
from datetime import datetime
from .sample_scheduler import SampleScheduler
class TestSampleScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = SampleScheduler()
    def test_get_level_config(self):
        self._level_0_test()
        self._level_1_test()
        self._level_2_test()
        self._level_3_test()
        self._level_4_test()
    def _level_0_test(self):
        datetime_list = [
            datetime(2018, 1, 3, 15, 32, 11),
            datetime(2018, 7, 4, 19, 56, 35)
        ]
        for d in datetime_list:
            self.assertEqual(self.scheduler.get_level_config(d).get_level(), 0)
    def _level_1_test(self):
        datetime_list = [
            datetime(2018, 3, 7, 0, 0, 0),
            datetime(2018, 5, 2, 0, 0, 0),
            datetime(2018, 9, 5, 0, 0, 0),
            datetime(2018, 11, 7, 0, 0, 0),
        ]
        for d in datetime_list:
            self.assertEqual(self.scheduler.get_level_config(d).get_level(), 1)
    def _level_2_test(self):
        datetime_list = [
            datetime(2018, 2, 7, 0, 0, 0),
            datetime(2018, 4, 4, 0, 0, 0),
            datetime(2018, 6, 6, 0, 0, 0),
            datetime(2018, 8, 1, 0, 0, 0),
            datetime(2018, 10, 3, 0, 0, 0),
            datetime(2018, 12, 5, 0, 0, 0),
        ]
        for d in datetime_list:
            self.assertEqual(self.scheduler.get_level_config(d).get_level(), 2)
    def _level_3_test(self):
        datetime_list = [
            datetime(2018, 3, 21, 0, 0, 0),
            datetime(2018, 1, 31, 0, 0, 0),
            datetime(2018, 8, 8, 0, 0, 0),
        ]
        for d in datetime_list:
            self.assertEqual(self.scheduler.get_level_config(d).get_level(), 3)
    def _level_4_test(self):
        datetime_list = [
            datetime(2018, 8, 2, 0, 0, 0),
            datetime(2018, 7, 3, 0, 0, 0),
            datetime(2018, 7, 5, 0, 0, 0),
            datetime(2018, 1, 7, 0, 0, 0),
            datetime(2018, 1, 1, 0, 0, 0),
        ]
        for d in datetime_list:
            self.assertEqual(self.scheduler.get_level_config(d).get_level(), 4)
    