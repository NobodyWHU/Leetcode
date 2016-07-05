class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        t = self.gcd(x, y)
        if t == 0:
            return z == 0
        return z%t == 0 and z <= x+y
    
    
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b%a, a)