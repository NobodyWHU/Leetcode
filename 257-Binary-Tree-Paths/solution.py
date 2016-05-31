# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        self.dfs(root, str(root.val), res)
        return res
    
    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path)
        if root.left:
            self.dfs(root.left, path+"->"+str(root.left.val), res)
        if root.right:
            self.dfs(root.right, path+"->"+str(root.right.val), res)
        