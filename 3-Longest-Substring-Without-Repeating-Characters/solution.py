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
        for i in range(n):
            temp = set()
            temp.add(s[i])
            for j in range(i+1, n):
                if s[j] in temp:
                    i = i+j
                    break
                else:
                    temp.add(s[j])
            ans = max(len(temp), ans)
        return ans