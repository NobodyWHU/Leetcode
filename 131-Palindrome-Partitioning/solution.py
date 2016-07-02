class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        self.dfs(s, [], ans)
        return ans
    
    def dfs(self, s, temp, ans):
        if len(s) == 0:
            ans.append(temp)
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], temp+[s[:i]], ans)
    
    def is_palindrome(self, s):
        return s == s[::-1]