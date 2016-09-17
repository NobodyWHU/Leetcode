class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        ans = []
        for i in range(n):
            temp = A[n-i:]+A[:n-i]
            v = 0
            p = 0
            for t in temp:
                v += p*t
                p += 1
            ans.append(v)
        return max(ans)
        