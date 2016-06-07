import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic = dict(zip(list(string.uppercase), range(1,27)))
        ans, base = 0, 1
        for char in s[::-1]:
            ans += dic[char] * base
            base *= 26
        
        return ans
            