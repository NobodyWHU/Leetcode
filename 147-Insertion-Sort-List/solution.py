# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummpy = ListNode(-1)
        dummpy.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummpy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = cur.next.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return dummpy.next
        