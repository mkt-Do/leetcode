class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def decode(self, l: ListNode) -> int:
        n = 0
        d = 0
        while l != None:
            n += l.val * pow(10, d)
            d += 1
            l = l.next
        return n

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.decode(l1)
        n2 = self.decode(l2)
        n = n1 + n2
        if n == 0:
            return ListNode(0)
        nums = []
        while n != 0:
            nums.append(n % 10)
            n //= 10
        l = None
        next = None
        for v in reversed(nums):
            l = ListNode(v, next)
            next = l
        return l
