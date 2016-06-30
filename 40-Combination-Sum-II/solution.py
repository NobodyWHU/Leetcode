class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        ans = []
        n = len(candidates)
        candidates.sort()
        self.helper(0, n, target, candidates, [], ans)
        return ans
        
    def helper(self, start, n, target, candidates, temp, ans):
        if target < 0:
            return
        if target == 0 and temp not in ans:
            ans.append(temp)
            return
        for i in range(start, n):
            self.helper(i+1, n, target-candidates[i], candidates, temp+[candidates[i]], ans)