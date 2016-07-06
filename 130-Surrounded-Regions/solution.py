class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x < 0 or x > m-1 or y < 0 or y > n-1 or board[x][y] != 'O':
                return
            queue.append((x,y))
            board[x][y] = 'D'

        def bfs(x, y):
            if board[x][y]=='O':
                queue.append((x,y))
                fill(x,y)

            while queue:
                curr = queue.pop(0)
                i, j = curr[0], curr[1]
                fill(i+1, j)
                fill(i-1, j)
                fill(i, j+1)
                fill(i, j-1)

        if len(board) == 0:
            return
        m, n , queue = len(board), len(board[0]), []
        for i in range(n):
            bfs(0, i)
            bfs(m-1, i)

        for j in range(1, m-1):
            bfs(j, 0)
            bfs(j, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            