class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(1, k, n, [], res)
        return res
        
    def helper(self, start, k, left_value, temp_list, res):
        if left_value == 0 and len(temp_list) == k:
            res.append(temp_list)
            return
        for i in range(start, min(10,left_value+1)):
            self.helper(i+1, k, left_value-i, temp_list+[i], res)
            