# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.toInt(l1) + self.toInt(l2)

    def toInt(self, l):
        res = 0
        i = 0
        while True:
            res += l.val * (10**i)
            i++
            if (l.next is None):
                return res
