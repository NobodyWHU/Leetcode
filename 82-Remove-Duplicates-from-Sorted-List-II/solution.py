# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = set()
        p, q = dummy.next, dummy
        while p:
            if p.val in temp:
                q.next = p.next
                p = p.next
            else:
                temp.add(p.val)
                p = p.next
                q = q.next
        j, k = dummy, dummy.next
        while k:
            if k.val in temp:
                j.next = k.next
            else:
                j = j.next
                k = k.next
        return dummy.next