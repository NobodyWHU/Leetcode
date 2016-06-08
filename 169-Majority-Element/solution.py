class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        majority = nums[0]
        for i in range(1, len(nums)):
            if majority == nums[i]:
                count += 1
            else:
                if count == 0:
                    count = 1
                    majority = nums[i]
                else:
                    count -= 1
        
        return majority