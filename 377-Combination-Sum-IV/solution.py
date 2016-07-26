class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        start = min(nums)
        if start > target:
            return 0
        # record number of combinations for i
        dp = [1] + [0] * target
        for i in range(len(dp)):
            # skip numbers that have no combinations
            if dp[i] != 0:
                for n in nums:
                    if i + n < len(dp):
                        dp[i + n] += dp[i]
        return dp[-1]