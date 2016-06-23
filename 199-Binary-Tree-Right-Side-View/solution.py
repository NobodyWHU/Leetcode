# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        valuemap = {}
        self.helper(root, valuemap, 0)
        ans = []
        depth = 0
        while depth in valuemap:
            ans.append(valuemap[depth])
            depth += 1
        return ans
    
    def helper(self, root, valuemap, depth):
        if not root:
            return
        valuemap[depth] = root.val
        self.helper(root.left, valuemap, depth+1)
        self.helper(root.right, valuemap, depth+1)