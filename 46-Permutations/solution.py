class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [nums]
        for i in range(len(nums)-1):
            for one in result[:]:
                for j in range(i+1, len(nums)):
                    result.append(one[:i] + one[j:] + one[i:j])
        return result