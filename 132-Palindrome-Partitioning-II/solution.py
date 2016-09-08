class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        # 以第i个字符开头到最后一个字符，一共有dp[i]个回文串
        dp = [l-i for i in range(l+1)]
        status = [[False]*l for _ in range(l)]
        for i in range(l-2, -1, -1):
            for j in range(i, l):
                if s[i] == s[j] and ((j - i) < 2 or status[i+1][j-1]):
                    status[i][j] = True
                    dp[i] = min(dp[j+1]+1, dp[i])
        return dp[0]-1