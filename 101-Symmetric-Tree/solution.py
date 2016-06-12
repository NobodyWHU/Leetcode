# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, leftNode, rightNode):
        if leftNode is None :
            return rightNode is None
        if rightNode is None:
            return leftNode is None
        if leftNode.val != rightNode.val:
            return False
        return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
        
        