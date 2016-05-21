class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pre, current = 0, 0
        while current < len(nums):
            if nums[current] == 0:
                current += 1
            else:
                nums[pre] = nums[current]
                pre += 1
                current += 1
        for i in range(pre, len(nums)):
            nums[i] = 0
        