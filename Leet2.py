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
            return    

        # If one of the lists is longer, we just need to append the tail
        if l1 is None:
            curr.next = l2.next
            return

        if l2 is None:
            curr.next = l1.next
            return 

        v = l1.val + l2.val + carry
        newCarry = v / 10
        next = ListNode(v % 10)
        curr.next = next
        self.computeNext(next, l1.next, l2.next, newCarry)
