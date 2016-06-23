# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = {}
        ans = self.dfs(root, m)
        return ans
    
    def dfs(self, root, m):
        if not root:
            return 0
        if root in m:
            return m[root]
        val = 0
        if root.left:
            val += self.dfs(root.left.left, m) + self.dfs(root.left.right, m)
        if root.right:
            val += self.dfs(root.right.left, m) + self.dfs(root.right.right, m)
        val = max(val+root.val, self.dfs(root.left, m)+self.dfs(root.right, m))
        m[root] = val
        return val
            