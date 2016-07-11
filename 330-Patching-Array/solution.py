class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        upper = 1
        miss = 0
        idx = 0
        while upper <= n:
            if idx < len(nums) and nums[idx] <= upper:
                upper += nums[idx]
                idx += 1
            else:
                upper += upper
                miss += 1
        return miss
        