class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def isLeadingZeros(num):
            return num.startswith("00") or int(num) and num.startswith("0")
        
        def helper(num, target, tmp, currRes, preNum, res):
            if currRes == target and len(num) == 0:
                res.append(tmp)
                return
            for i in range(1, len(num)+1):
                currStr = num[:i]
                if isLeadingZeros(currStr):
                    return
                currNum = int(currStr)
                nextStr = num[i:]
                if len(tmp)!=0:
                    helper(nextStr, target, tmp+"*"+currStr, (currRes-preNum)+preNum*currNum, preNum*currNum, ans)
                    helper(nextStr, target, tmp+"+"+currStr, currRes+currNum, currNum, ans)
                    helper(nextStr, target, tmp+"-"+currStr, currRes-currNum, -currNum, ans)
                else:
                    helper(nextStr, target, currStr, currNum, currNum, ans)
        
        ans = []
        helper(num, target, "", 0, 0, ans)
        return ans