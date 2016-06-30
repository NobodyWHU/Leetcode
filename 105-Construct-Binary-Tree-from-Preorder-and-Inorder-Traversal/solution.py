# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.itable = {v:i for i, v in enumerate(inorder)}
        return self.Build(0, 0, len(preorder))

    def Build(self, pbegin, ibegin, size):
        if not size: return None
        imid = self.itable[self.preorder[pbegin]]
        lsize = imid - ibegin
        rsize = size - lsize - 1
        tree = TreeNode(self.preorder[pbegin])
        tree.left = self.Build(pbegin + 1, ibegin, lsize)
        tree.right = self.Build(pbegin + 1 + lsize, imid + 1, rsize)
        return tree