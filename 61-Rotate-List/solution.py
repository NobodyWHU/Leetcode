# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k==0:
            return head
        p_temp = p_start = head
        value_num = 1
        while p_temp.next:
            value_num += 1
            p_temp = p_temp.next
        p_temp.next = head
        k = k % value_num
        step = value_num - k
        while step>1:
            p_start = p_start.next
            step = step - 1
        head = p_start.next
        p_start.next = None
        return head
        
        
        