# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val)
            listp.append(root)
            self.inorder(root.right, list, listp)
    def recoverTree(self, root):
        list = []
        listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]