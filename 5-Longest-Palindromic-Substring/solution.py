class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        ans = ""
        for i in range(len(s)):
            str1 = self.getLongestPalindrome(s, i, i)
            if len(str1) > len(ans):
                ans = str1
            str2 = self.getLongestPalindrome(s, i, i+1)
            if len(str2) > len(ans):
                ans = str2
        return ans
        
    def getLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]