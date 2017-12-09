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
        x = l1.val + l2.val
        node = ListNode(x % 10)
        self.computeNext(node, l1.next, l2.next, x / 10)
        return node

    def computeNext(self, curr, l1, l2, carry):
        # Assume they are the same length
        if l1 is None and l2 is None:
            if carry > 0:
                curr.next = ListNode(carry)
            return    

        v1 = 0 if l1 is None else l1.val
        v2 = 0 if l2 is None else l2.val

        v = v1 + v2 + carry
        newCarry = v / 10
        next = ListNode(v % 10)
        curr.next = next
        next1 = None if l1 is None else l1.next
        next2 = None if l2 is None else l2.next
        self.computeNext(next, next1, next2, newCarry)
