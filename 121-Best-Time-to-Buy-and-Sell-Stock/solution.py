class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        low_price = prices[0]
        max_pro = 0
        
        for i in range(1, n):
            low_price = min(low_price, prices[i])
            max_pro = max(max_pro, prices[i]-low_price)
        return max_pro
            