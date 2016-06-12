class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[] for i in range(numRows)]
        for i in range(numRows):
            res[i] = [1 for j in range(i+1)]
        
        for i in range(numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        
        return res
        