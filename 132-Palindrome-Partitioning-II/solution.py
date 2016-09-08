class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        self.dfs(s, [], ans)
        if not ans:
            return 0
        else:
            return min(len(v) for v in ans) - 1
    
    def dfs(self, s, temp, ans):
        if len(s) == 0:
            ans.append(temp)
            return
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], temp+[s[:i]], ans)
    
    def is_palindrome(self, s):
        return s == s[::-1]