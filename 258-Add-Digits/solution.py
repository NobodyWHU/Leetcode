class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        tmp = self.helper(num)
        while tmp >= 10:
            tmp = self.helper(tmp)
        return tmp
        
    def helper(self, num):
        res = 0
        while num/10:
            res += num%10
            num /= 10
        res += num
        return res