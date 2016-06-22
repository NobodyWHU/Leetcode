class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        n = len(prices)
        maxBuys = [0] * n
        maxSells = [0] * n
        
        buy, sell = 0, 0
        for i in range(n):
            if i >= 2:
                buy = -prices[i] + maxSells[i-2]
            else:
                buy = -prices[i]
            maxBuys[i] = buy if i == 0 else max(maxBuys[i-1], buy)
            
            sell = 0 if i == 0 else maxBuys[i-1] + prices[i]
            maxSells[i] = sell if i == 0 else max(maxSells[i-1], sell)
        
        return maxSells[n-1]