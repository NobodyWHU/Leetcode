# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.helper(root, 0, res)
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res
        
        
    def helper(self, node, level, res):
        if node:
            if len(res) < level+1:
                res.append([])
            res[level].append(node.val)
            self.helper(node.left, level+1, res)
            self.helper(node.right, level+1, res)
        