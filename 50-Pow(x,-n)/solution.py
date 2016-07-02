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
            if n & 1 == 1:
                ans *= x
            x *= x
            n >>= 1
        if flag:
            return ans
        else:
            return 1/ans