class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        sumv = 0
        for i in range(n):
            sumv += i * A[i]
        sumt = sum(A)
        ans = sumv
        for num in A:
            sumv += n*num-sumt
            ans = max(ans, sumv)
        return ans