# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        curr = root
        while curr:
            firstNodeInNextLevel = None
            prev = None
            while curr:
                if not firstNodeInNextLevel:
                    firstNodeInNextLevel = curr.left if curr.left else curr.right
                if curr.left:
                    if prev: prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev: prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            curr = firstNodeInNextLevel # turn to next level
        
        