class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not k or k <= 0:
            return
        k, end = k % len(nums), len(nums)
        self.reverse(nums, 0, end-k)
        self.reverse(nums, end-k, end)
        self.reverse(nums, 0, end)
    
    
    def reverse(self, nums, start, end):
        tmp = nums[start:end]
        nums[start:end] = tmp[::-1]
        