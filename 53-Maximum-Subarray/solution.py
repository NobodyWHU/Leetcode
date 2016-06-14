class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = nums[0]
        sum = 0
        for num in nums:
            sum += num
            ans = max(ans, sum)
            sum = max(sum, 0)
        return ans
        