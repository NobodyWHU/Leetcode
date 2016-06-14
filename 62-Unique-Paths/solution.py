class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        if m==1 or n==1:
            return 1
        res = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            res[i][0] = 1
        for j in range(n):
            res[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
        