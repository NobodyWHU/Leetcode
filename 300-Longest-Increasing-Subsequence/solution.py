class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for i in range(n)]
        
        for x in range(n):
            for y in range(x):
                if nums[x]>nums[y]:
                    dp[x] = max(dp[x], dp[y]+1)
        return max(dp)
        