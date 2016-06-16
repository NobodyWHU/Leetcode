class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                continue
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1