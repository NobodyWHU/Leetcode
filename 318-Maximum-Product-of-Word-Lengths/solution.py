class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0 for i in range(n)]
        for i, w in enumerate(words):
            for c in w:
                elements[i] |= 1<< (ord(c)-97)
        
        v_max = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (elements[i] & elements[j]):
                    v_max = max(v_max, len(words[i])*len(words[j]))
        return v_max
                    
        