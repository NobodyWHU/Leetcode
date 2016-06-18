class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, num in enumerate(nums):
            if (target-num) in table:
                return [table[target-num], i]
            if num not in table:
                table[num] = i
        
        return None