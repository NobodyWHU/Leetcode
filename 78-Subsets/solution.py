class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        def dfs(depth, start, valuelist):
            ret.append(valuelist)
            if len(valuelist) == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])
        dfs(0, 0, [])
        return ret
        