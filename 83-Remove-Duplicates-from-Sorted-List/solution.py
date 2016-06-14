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
        vset = set()
        p = head
        dummpy = ListNode(-1)
        dummpy.next = head
        q = dummpy
        while p:
            v = p.val
            if v in vset:
                q.next = p.next
                p = p.next
            else:
                vset.add(v)
                q = q.next
                p = p.next
        return dummpy.next
                
                