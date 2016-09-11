class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        maxval = [0]*n
        minval = [0]*n
        maxval[0]=minval[0]=nums[0]
        for i in range(1, n):
            maxval[i] = max(maxval[i-1]*nums[i], minval[i-1]*nums[i], nums[i])
            minval[i] = min(minval[i-1]*nums[i], maxval[i-1]*nums[i], nums[i])
        return max(max(maxval), max(minval))
        