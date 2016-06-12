# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        return self.genBST(1, n)
    
    
    def genBST(self, minv, maxv):
        ret = []
        if minv > maxv:
            ret.append(None)
            return ret
        for i in range(minv, maxv+1):
            leftTree = self.genBST(minv, i-1)
            rightTree = self.genBST(i+1, maxv)
            for j in range(len(leftTree)):
                for k in range(len(rightTree)):
                    node = TreeNode(i)
                    node.left = leftTree[j]
                    node.right = rightTree[k]
                    ret.append(node)
                    
        return ret