class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        if m != 9 or n != 9:
            return False
        
        def checkValid(valueList):
            temp = collections.defaultdict(int)
            for v in valueList:
                temp[v] += 1
            for k, v in temp.items():
                if k != "." and v > 1:
                    return False
            return True
        
        # check row
        for row in range(m):
            if not checkValid(board[row]):
                return False
        
        # check column
        for column in range(n):
            columnList = []
            for row in range(m):
                columnList.append(board[row][column])
            if not checkValid(columnList):
                return False
        
        
        # check square
        for i in range(3):
            for j in range(3):
                squareList = []
                for p in range(3):
                    for q in range(3):
                        squareList.append(board[i*3+q][j*3+p])
            
                if not checkValid(squareList):
                    return False
        
        
        return True