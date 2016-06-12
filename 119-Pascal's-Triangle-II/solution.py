class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        result = [[] for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            result[i] = [1 for _ in range(rowIndex+1)]
            for j in range(1, i):
                result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result[rowIndex]
        
        