class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or k == 0:
            return False
        temp = {}
        for i in range(len(nums)):
            if i > k:
                temp.pop(nums[i-k-1])
            if nums[i] not in temp:
                temp[nums[i]] = i
            else:
                return True
        return False