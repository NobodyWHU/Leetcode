class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        res = [0 for _ in range(n)]
        res[0] = nums[0]
        res[1] = max(nums[:2])
        for i in range(2, n):
            res[i] = max(res[i-1], nums[i]+res[i-2])
        return res[n-1]