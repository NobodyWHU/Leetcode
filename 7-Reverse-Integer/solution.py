class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        flag = 1
        if x < 0:
            flag = -1
        x= abs(x)
        x = int(str(x)[::-1])
        if x > 2147483647:
            return 0
        return flag*x
            