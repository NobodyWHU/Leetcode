class Solution(object):
    def live_nbrs(self,board,i,j,m,n):
        ms=max(0,i-1)
        ns=max(0,j-1)
        me=min(m,i+2)
        ne=min(n,j+2)
        count=0
        for i1 in xrange(ms,me):
            for j1 in xrange(ns,ne):
                if board[i1][j1]&1:
                    count+=1
        return count-(board[i][j]&1)
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m=len(board)
        if not m:
            return
        n=len(board[0])
        lm,ln=map(xrange,[m,n])
        for i in lm:
            for j in ln:
                num=self.live_nbrs(board,i,j,m,n)
                if not (board[i][j]&1):
                    board[i][j]=bool(num==3)<<1
                else:
                    board[i][j]+=bool(num not in [2,3])<<1
        for i in lm:
            for j in ln:
                board[i][j]=((board[i][j]&2)>>1)^(board[i][j]&1)