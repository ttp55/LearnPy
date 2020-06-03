# @Time : 2019/12/24 15:16
# @Author : WZG
# --coding:utf-8--
import unittest


def s_sum(min, max):
    return sum([i for i in range(min, max)])


class TestSum(unittest.TestCase):
    def test_init(self):
        d = s_sum(0, 100)
        self.assertEqual(d, 4950)
