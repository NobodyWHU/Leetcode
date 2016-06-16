class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k=0
            tmp = divisor
            while dividend >= tmp:
                quotient += 1<<k
                dividend -= tmp
                tmp <<= 1
                k += 1
        res = quotient * sign
        if res > 2147483647:
            return 2147483647
        else:
            return res
        