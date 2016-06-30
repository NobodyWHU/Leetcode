class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return True
        maxval = 0
        for i in range(n):
            if i > maxval:
                return False
            maxval = max(maxval, i+nums[i])
        return True