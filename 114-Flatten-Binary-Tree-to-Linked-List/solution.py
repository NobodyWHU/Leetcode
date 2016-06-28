# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        allnode = []
        self.preorder(root, allnode)
        for i, node in enumerate(allnode[:-1]):
            node.left = None
            node.right = allnode[i+1]
        allnode[-1].left = None
        allnode[-1].right = None
    
    def preorder(self, root, allnode):
        if not root:
            return
        allnode.append(root)
        self.preorder(root.left, allnode)
        self.preorder(root.right, allnode)
        