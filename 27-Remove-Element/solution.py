class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num = 0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[num]=nums[i]
                num += 1
        return num
        