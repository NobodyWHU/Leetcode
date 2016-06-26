class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(n,k,1,[], ans)
        return ans
    
    def helper(self, n, k, start, temp_list, ans):
        if len(temp_list) == k:
            ans.append(temp_list)
            return
        for i in range(start, n+1):
            self.helper(n, k, i+1, temp_list+[i], ans)