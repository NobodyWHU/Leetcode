class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        s = s.lower()
    
        while left < right:
            while not s[left].isalnum() and left < right: left += 1
            while not s[right].isalnum() and left < right: right -= 1
    
            if s[left] != s[right]: return False
            else:
                left += 1
                right -= 1
    
        return True
        