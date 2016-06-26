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
        if 0 == k:
            ans.append(temp_list)
            return
        for i in range(start, n-k+2):
            self.helper(n, k-1, i+1, temp_list+[i], ans)