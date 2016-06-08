class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            else:
                mid = (left + right) / 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]
        