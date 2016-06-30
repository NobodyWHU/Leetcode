# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.helper(sum-root.val, root, [root.val], ans)
        return ans
    
    
    def helper(self, leftvalue, root, temp, ans):
        if leftvalue == 0 and root.left is None and root.right is None:
            ans.append(temp)
            return
        if root.left:
            self.helper(leftvalue-root.left.val, root.left, temp+[root.left.val], ans)
        if root.right:
            self.helper(leftvalue-root.right.val, root.right, temp+[root.right.val], ans)
        