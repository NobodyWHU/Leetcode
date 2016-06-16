class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, ans = 5, 0
        while k <= n:
            ans += n / k
            k *= 5
        return ans