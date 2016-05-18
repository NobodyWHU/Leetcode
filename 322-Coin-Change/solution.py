class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            if dp[i]<0:
                continue
            for c in coins:
                if i+c > amount:
                    continue
                if dp[i+c]<0 or dp[i]+1<dp[i+c]:
                    dp[i+c] = dp[i]+1
        return dp[amount]
        