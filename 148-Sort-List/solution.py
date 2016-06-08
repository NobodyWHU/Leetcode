# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p1, p2 = head, slow.next
        slow.next = None
        sortedp1 = self.sortList(p1)
        sortedp2 = self.sortList(p2)
        head = self.merge(sortedp1, sortedp2)
        return head
    
    def merge(slef, p1, p2):
        if not p1:
            return p2
        if not p2:
            return p1
        dummpy = ListNode(-1)
        p = dummpy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummpy.next
        