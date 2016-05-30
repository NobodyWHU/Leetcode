class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1]
        q2, q3, q5 = 0, 0, 0
        while len(l) < n:
            m2, m3, m5 = l[q2]*2, l[q3]*3, l[q5]*5
            m = min(m2, m3, m5,)
            if m == m2:
                q2 +=1
            if m == m3:
                q3 += 1
            if m == m5:
                q5 += 1
            l.append(m)
        return l[-1]