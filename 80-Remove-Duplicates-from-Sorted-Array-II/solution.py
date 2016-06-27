class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n
        end = 1
        for i in range(2, n):
            if nums[i] != nums[end-1]:
                end += 1
                nums[end] = nums[i]
        
        return end + 1