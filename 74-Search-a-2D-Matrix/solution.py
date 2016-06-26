class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        low, high = 0, m*n-1
        while low <= high:
            mid = (low+high)/2
            val = matrix[mid/n][mid%n]
            
            if target > val:
                low = mid +1
            elif target < val:
                high = mid -1
            else:
                return True
        
        return False