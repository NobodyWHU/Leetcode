class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[k/fac]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res