class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        n = len(nums)
        nums.sort()
        dp = [1] * n
        index = [-1] * n
        max_dp, max_index = 1, 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j
            
            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i
        
        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = index[max_index]
        return ans
        