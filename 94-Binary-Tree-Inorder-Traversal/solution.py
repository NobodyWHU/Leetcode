# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        self.inorder(root, ret)
        return ret
    
    
    def inorder(self, root, ret):
        if not root:
            return ret
        
        self.inorder(root.left, ret)
        ret.append(root.val)
        self.inorder(root.right, ret)
        
        