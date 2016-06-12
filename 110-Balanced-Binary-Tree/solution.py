# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def Height(self, root):
        if root == None:
            return 0
        return max( self.Height( root.left ), self.Height( root.right ) ) + 1
    
    def isBalanced(self, root):
        if root  == None:
            return True
        if abs( self.Height( root.left ) - self.Height( root.right ) ) <= 1:
            return self.isBalanced( root.left ) and self.isBalanced( root.right )
        else:
            return False
        