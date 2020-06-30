from leetcode.two_sum import TwoSum
import unittest

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(TwoSum().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(TwoSum().twoSum([3, 3], 6), [0, 1])
