class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        neg = False
        s = s.lstrip()
        if len(s)> 0 and (s[0] == '+' or s[0] == '-'): # deal with positive/negative sign
            if s[0] == '-':
                neg = True
            s = s[1:]
        i = 0
        while i < len(s) and ord(s[i]) in range(48, 58): # deal with digits
            i += 1
        r = 0
        if i > 0:
            r = int(s[:i])
        if neg:
            r *= -1
        return max(min(r, pow(2, 31)-1), -pow(2, 31))