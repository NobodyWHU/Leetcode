# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n ==1 or n == 0:
            return head
        
        i = 0
        result = head
        newhead = ListNode(0)
        newhead.next = head
        
        while i < m-1:
            newhead = newhead.next
            i += 1
        
        reverseLinkList = newhead.next
        preConnect = newhead
        
        while i < n:
            newhead = newhead.next
            i += 1
        secStart = newhead.next
        reverseStart = newhead
        
        reverseStart.next = None
        preConnect.next = None
        
        self.reverse(reverseLinkList)
        preConnect.next = reverseStart
        reverseLinkList.next = secStart
        
        if m == 1:
            return reverseStart
        return result
    
    
    def reverse(self, head):
        p = None
        while head is not None:
            newhead = head.next
            head.next = p
            p = head
            head = newhead
        return p
        