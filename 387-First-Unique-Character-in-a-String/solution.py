class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        from collections import Counter
        c = Counter(s)
        for i in range(len(s)):
            if c.get(s[i]) <= 1:
                return i
        return -1