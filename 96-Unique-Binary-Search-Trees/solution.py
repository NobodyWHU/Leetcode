class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        ans = 0
        for i in range(0, n):
            ans += self.numTrees(i)*self.numTrees(n-i-1)
        return ans