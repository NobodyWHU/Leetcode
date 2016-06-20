class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        begin, end = 1, 1
        ans = [1] * len(nums)
        n = len(nums)
        for i, num in enumerate(nums):
            ans[i] *= begin
            begin *= num
            ans[n-i-1] *= end
            end *= nums[n-i-1]
        return ans
        