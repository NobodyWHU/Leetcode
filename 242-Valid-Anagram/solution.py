class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_l = list(sorted(s))
        t_l = list(sorted(t))
        return s_l == t_l