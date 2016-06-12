# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from sys import maxint
        if not root:
            return True
        return self.valid(root, -maxint-2, maxint)
    
    def valid(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.valid(root.left, minVal, root.val) and self.valid(root.right, root.val, maxVal)
        