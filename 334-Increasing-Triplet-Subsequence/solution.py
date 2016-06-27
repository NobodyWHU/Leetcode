class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        nmin = nmid = float("Inf")
        
        for i in nums:
            if i > nmid:
                return True
            if nmin < i < nmid:
                nmid = i
            if i < nmin:
                nmin = i
        return False
        
        