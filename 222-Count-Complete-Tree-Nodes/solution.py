# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        if not root:
            return 0
        left, right = root, root
        numl, numr = 0, 0
        while left:
            numl += 1
            left = left.left
        while right:
            numr += 1
            right = right.right
        if numl == numr:
            return int(math.pow(2, numl))-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        