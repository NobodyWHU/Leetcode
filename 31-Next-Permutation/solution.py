class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        partition = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                partition = i
                break
        if partition == -1:
            return nums.reverse()
        else:
            for i in range(len(nums)-1,partition,-1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition+1:] = nums[partition+1:][::-1]