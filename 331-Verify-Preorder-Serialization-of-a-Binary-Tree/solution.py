class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == "": return False
        preorder += ","
        l = len(preorder)
        capacity = 1
        for i in range(l):
            if preorder[i] != ",":
                continue
            capacity -= 1
            if capacity < 0:
                return False
            if preorder[i-1] != "#":
                capacity += 2
            
        return capacity == 0
        