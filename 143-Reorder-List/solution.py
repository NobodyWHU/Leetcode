# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        head_slow = head
        head_fast = slow.next
        slow.next = None

        
       # reverse fast list
        cur = head_fast
        post = head_fast.next
        head_fast.next = None
        while post:
            temp = post.next
            post.next = cur
            cur = post
            post = temp
        head_fast = cur
        
        # merge two list
        p = head_slow
        q = head_fast
        while q:
            temp1 = p.next
            temp2 = q.next
            p.next = q
            q.next = temp1
            p = temp1
            q = temp2
        
        