class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return None
        l = self.findLeftMost(nums, n, target)
        r = self.findRightMost(nums, n, target)
        return [l, r]
    
    
    def findLeftMost(self, nums, n, target):
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) / 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if start >= 0 and start < n and nums[start] == target:
            return start
        return -1
    
    
    def findRightMost(self, nums, n, target):
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) / 2
            if target < nums[mid]:
                end = mid -1
            elif target > nums[mid]:
                start = mid + 1
            else:
                start = mid + 1
        if end >= 0 and end < n and nums[end] == target:
            return end
        return -1