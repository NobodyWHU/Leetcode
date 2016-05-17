class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        the factor should be less than 4, we should use 3 as many as possible
        """
        if n == 2: return 1
        if n == 3: return 2
        product = 1
        while(n>4):
            product *= 3
            n -= 3
        product *= n
        return product
        