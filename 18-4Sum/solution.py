class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, res, d = len(nums), set(), {}
        if numLen < 4:
            return []
        nums.sort()
        for p in range(numLen):
            for q in range(p+1, numLen):
                if nums[p] + nums[q] in d:
                    d[nums[p] + nums[q]].append((p, q))
                else:
                    d[nums[p] + nums[q]] = [(p, q)]
        
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                t = target - nums[i] - nums[j]
                if t in d:
                    for k in d[t]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]