class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        i = 1
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 1
        return False