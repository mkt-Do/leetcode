from leetcode.add_two_numbers import AddTwoNumbers, ListNode
from typing import List
import unittest

class TestAddTwoNumbers(unittest.TestCase):
    def generate_listnode(self, l: List) -> ListNode:
        next = None
        for v in reversed(l):
            node = ListNode(v, next)
            next = node
        return next

    def test_addTwoNumbers(self):
        l1 = self.generate_listnode([2, 4, 3])
        l2 = self.generate_listnode([5, 6, 4])
        ept = self.generate_listnode([7, 0, 8])
        act = AddTwoNumbers().addTwoNumbers(l1, l2)
        while (act.next != None):
            self.assertEqual(act.val, ept.val)
            act = act.next
            ept = ept.next
