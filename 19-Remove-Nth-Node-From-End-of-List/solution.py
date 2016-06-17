# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        temp = head
        while n:
            if temp:
                temp = temp.next
            else:
                return head
            n -= 1
        slow = dummy
        while temp:
            slow = slow.next
            temp = temp.next
        slow.next = slow.next.next
        return dummy.next
        
        