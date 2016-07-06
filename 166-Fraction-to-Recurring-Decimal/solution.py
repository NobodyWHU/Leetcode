class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        numList = []
        cnt = 0
        loopDict = {}
        loopStr = None
        while True:
            numList.append(str(numerator/denominator))
            cnt += 1
            numerator = 10 * (numerator%denominator)
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numList[loc:cnt])
                break
            loopDict[numerator] = cnt
        ans = numList[0]
        if len(numList) > 1:
            ans += "."
        if loopStr:
            ans += "".join(numList[1:len(numList)-len(loopStr)]) + "("+loopStr+")"
        else:
            ans += "".join(numList[1:])
        if flag:
            ans = "-" + ans
        return ans
        