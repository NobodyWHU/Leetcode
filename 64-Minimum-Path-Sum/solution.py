class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        ans[0][0] = grid[0][0]
        for i in range(1, n):
            ans[0][i] = grid[0][i] + ans[0][i-1]
        for i in range(1, m):
            ans[i][0] = grid[i][0] + ans[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i-1][j], ans[i][j-1]) + grid[i][j]
        return ans[m-1][n-1]