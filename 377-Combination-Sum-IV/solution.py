class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = []
        self.helper(nums, target, [], ans)
        return len(ans)
        
    def helper(self, nums, leftvalue, templist, ans):
        if leftvalue == 0:
            ans.append(templist)
            return
        if leftvalue < 0:
            return
        for i in nums:
            self.helper(nums, leftvalue-i, templist+[i], ans)