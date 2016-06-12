# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.preNum(root, 0)
    
    def preNum(self, root, pre):
        if not root:
            return 0
        pre = pre*10+root.val
        if not root.left and not root.right:
            return pre
        return self.preNum(root.left,pre) + self.preNum(root.right, pre)
        