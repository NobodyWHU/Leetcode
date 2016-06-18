class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        c = 1
        primeFlag = [False] * (n+1)
        
        i = 3
        while i*i <= n:
            if primeFlag[i]:
                continue
            j = i**2
            while j <= n:
                primeFlag[j] = True
                j += i
            i = i + 2
        
        for i in range(3, n, 2):
            if not primeFlag[i]:
                c += 1
        
        
        return c