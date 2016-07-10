class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result = 1
        for digit in b:
            result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
        return result