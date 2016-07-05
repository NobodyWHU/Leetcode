class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        ans = -1
        start = 0
        used_dict = {}
        for i in range(n):
            if s[i] in used_dict and start <= used_dict[s[i]]:
                start = used_dict[s[i]] + 1
            else:
                ans = max(ans, i-start+1)
            
            used_dict[s[i]] = i
        
        return ans