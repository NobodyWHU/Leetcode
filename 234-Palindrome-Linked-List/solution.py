# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        return p1 is None