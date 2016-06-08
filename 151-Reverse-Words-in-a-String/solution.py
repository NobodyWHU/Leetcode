class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s.split(" ")) == 0:
            return ""
        return " ".join(t for t in s.split(" ")[::-1] if len(t)>0)