class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = L + ((R - L) >> 1)
            temp = sum([self.binary_search(y,mid,n) for y in matrix])
            if temp < k:  L = mid + 1
            else:  R = mid
        return L
 
    def binary_search(self, row, x, n):
        L, R = 0, n
        while L < R:
            mid = (L + R) >> 1
            if row[mid] <= x: L = mid + 1
            else:  R = mid
        return L