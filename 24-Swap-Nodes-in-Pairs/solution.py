# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        fakehead = ListNode(0)
        fakehead.next = head
        pr1 = fakehead
        pr2 = head
        while pr2 and pr2.next:
            nextstart = pr2.next.next
            pr2.next.next = pr2
            pr1.next = pr2.next
            pr2.next = nextstart
            pr1 = pr2
            pr2 = nextstart
        return fakehead.next