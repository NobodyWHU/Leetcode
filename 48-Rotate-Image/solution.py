class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = temp
        
        for i in range(n/2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-i-1][j]
                matrix[n-i-1][j] = temp