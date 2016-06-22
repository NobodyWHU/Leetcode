class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dic = {}
        return self.getSums(input, dic)
        
    def getSums(self, string, dic):
        res = []
        sign = False
        if string in dic:
            return dic[string]
        
        for i, c in enumerate(string):
            if c == "+" or c == "-" or c == "*":
                sign = True
                fore = string[:i]
                after = string[i+1:]
                foreSums = self.getSums(fore, dic)
                afterSums = self.getSums(after, dic)
                for fsum in foreSums:
                    for asum in afterSums:
                        r = self.compute(fsum, c, asum)
                        res.append(r)
                        dic[string] = res
        if not sign:
            return [int(string)]
            
        return res
    
    def compute(self, a, c, b):
        if c == "+":
            return a+b
        elif c == "-":
            return a-b
        else:
            return a*b
    