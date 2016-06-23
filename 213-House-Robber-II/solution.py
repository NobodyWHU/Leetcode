class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        l1 = self.helper(nums[:-1])
        l2 = self.helper(nums[1:])
        return max(l1, l2)
    
    def helper(self, temp):
        if len(temp) == 0:
            return 0
        if len(temp) < 3:
            return max(temp)
        ans = [0] * len(temp)
        ans[0] = temp[0]
        ans[1] = max(temp[:2])
        for i in range(2, len(temp)):
            ans[i] = max(ans[i-1], ans[i-2]+temp[i])
        return ans[len(temp)-1]
        