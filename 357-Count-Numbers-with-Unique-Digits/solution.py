class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        dp = [0]*n
        dp[0] = 9
        for i in range(1,n):
            dp[i] = dp[i-1] * (10-i)
        
        return sum(dp) + 1
        