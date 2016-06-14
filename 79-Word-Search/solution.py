from collections import defaultdict

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if self._hasEnougnCharacter(board, word):
            m = len(board)
            n = len(board[0])
            for i in range(m):
                for j in range(n):
                    if self._exist(board, i,j,m,n,word):
                        return True
            return False
        else:
            return False
        
        
    def _hasEnougnCharacter(self, board, word):
        character_counts = defaultdict(int)
        for ch in word:
            character_counts[ch] +=1
        return all(sum(map(lambda line: line.count(ch), board)) >= count for ch, count in character_counts.items())
    
    def _exist(self, board, i, j, m, n, word):
        if len(word) == 0:
            return True
        if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = "."
        next_target = word[1:]
        next_result = self._exist(board,i-1,j,m,n,next_target) \
                      or self._exist(board,i,j-1,m,n,next_target)\
                      or self._exist(board,i+1,j,m,n,next_target)\
                      or self._exist(board,i,j+1,m,n,next_target)
        board[i][j] = temp
        return next_result