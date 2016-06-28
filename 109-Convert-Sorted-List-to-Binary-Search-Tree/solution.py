# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        listNum = 0
        cur = head
        while cur:
            listNum += 1
            cur = cur.next
        self.flag = head
        return self.helper(0, listNum - 1)
    
    def helper(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        leftChild = self.helper(start, mid -1)
        cur = TreeNode(self.flag.val)
        self.flag = self.flag.next
        rightChild = self.helper(mid + 1, end)
        cur.left = leftChild
        cur.right = rightChild
        return cur