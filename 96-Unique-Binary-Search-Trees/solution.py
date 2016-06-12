class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        dp = [ 0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            mid = i // 2
            for j in range(0, mid):
                dp[i] += (dp[j] * dp[i-1-j]) * 2
            if i % 2 == 1:
                dp[i] += dp[mid] ** 2
        return dp[-1]