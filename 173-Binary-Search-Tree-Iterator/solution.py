# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.sorted_list = []
        self._helper(root, self.sorted_list)
        self.flag = -1
        self.size = len(self.sorted_list)
    
    def _helper(self, root, sorted_list):
        if not root:
            return None
        
        self._helper(root.left, self.sorted_list)
        self.sorted_list.append(root.val)
        self._helper(root.right, self.sorted_list)
        
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self.flag += 1
        return self.flag < self.size
        

    def next(self):
        """
        :rtype: int
        """
        
        return self.sorted_list[self.flag]
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())