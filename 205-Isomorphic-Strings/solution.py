class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        ds, dt = {}, {}
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            if cs not in ds and ct not in dt:
                ds[cs] = ct
                dt[ct] = cs
            else:
                if cs in ds and ct in dt and ds[cs] == ct and dt[ct] == cs:
                    continue
                else:
                    return False
        return True
        
        