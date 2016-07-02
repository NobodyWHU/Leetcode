class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        ans = 1
        flag = n > 0
        n = abs(n)
        while n:
            ans *= x
            n -= 1
        if flag:
            return ans
        else:
            return 1/ans