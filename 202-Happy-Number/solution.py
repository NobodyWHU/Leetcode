class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp_set = set()
        while n != 1:
            if n not in tmp_set:
                tmp_set.add(n)
            else:
                return False
            sum = 0
            while n != 0:
                sum += (n%10)**2
                n /= 10
            n = sum
        return True