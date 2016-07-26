# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        Solution.max = -sys.maxint-1
        if root is None:
            return 0
        self.maxsum(root)
        return Solution.max
        
    
    def maxsum(self, root):
        if root is None:
            return 0
        ret = root.val
        lmax, rmax = 0, 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                ret += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                ret += rmax
        if ret > Solution.max:
            Solution.max = ret
        return max(root.val, max(root.val+lmax, root.val+rmax))