class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res, histRow = 0, [0 for _ in matrix[0]] if matrix else None
        for rowNums in matrix:
            stk = []
            for c, num in enumerate(rowNums):
                histRow[c] = histRow[c]+1 if num == "1" else 0
            for i, n in enumerate(histRow+[0]):
                while stk and histRow[stk[-1]] > n:
                    h = histRow[stk.pop()]
                    res = max(res, h*(i-stk[-1]-1 if stk else i))
                stk.append(i)
        return res
        