class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        c = Counter(magazine)
        for t in ransomNote:
            if t not in c:
                return False
            if c.get(t) <= 0:
                return False
            c[t] -= 1
        return True
            