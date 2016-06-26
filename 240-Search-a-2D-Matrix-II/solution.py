class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        if n==0:
            return False
        m=len(matrix[0])
        if m==0:
            return False
        i,j=0,m-1
        while i<n and j>-1:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False