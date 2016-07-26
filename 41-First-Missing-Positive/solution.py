class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        if n == 0:
            return 1
        while i < n:
            while nums[i] != i+1 and nums[i] <= n and nums[i] > 0 and nums[i] != nums[nums[i]-1]:
                t = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[t-1] = t
            i = i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        return n+1