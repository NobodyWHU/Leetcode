class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict
        bulls, cows = 0, 0
        s, g = defaultdict(int), defaultdict(int)
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
            s[int(secret[i])] += 1
            g[int(guess[i])] += 1
        for i in range(10):
            cows += min(s[i], g[i])
        
        return str(bulls)+"A"+str(cows-bulls)+"B"
        
        