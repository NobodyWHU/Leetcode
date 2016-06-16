class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sym = {
        1:'I', 5:'V',
        10:'X', 50:'L',
        100:'C', 500:'D',
        1000:'M'
        }
        rv, i = '', 1
        while num:
            mod = num % 10
            if mod in range(1,4):
                rv = mod*sym[i] + rv
            elif mod == 4:
                rv = sym[i]+sym[5*i] + rv
            elif mod == 5:
                rv = sym[5*i] + rv
            elif mod in range(6,9):
                rv = sym[5*i] + (mod-5)*sym[i] + rv
            elif mod == 9:
                rv = sym[i] + sym[10*i] + rv
            i *= 10
            num /= 10
        return rv