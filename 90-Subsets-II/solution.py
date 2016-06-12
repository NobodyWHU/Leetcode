class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        prevalue = None
        def dfs(depth, start, valuelist):
            if valuelist not in ret:
                ret.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])
        dfs(0, 0, [])
        return ret