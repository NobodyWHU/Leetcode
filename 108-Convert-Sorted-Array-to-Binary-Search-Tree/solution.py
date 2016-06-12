# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        tree = self.buildTree(nums, 0, len(nums)-1)
        return tree
    
    def buildTree(self, nums, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, start, mid-1)
        root.right = self.buildTree(nums, mid+1, end)
        return root
        