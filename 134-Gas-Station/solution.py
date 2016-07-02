class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        for i in range(n):
            flag = True
            mygas = 0
            for j in range(n):
                mygas = mygas + gas[(i+j)%n] - cost[(i+j)%n]
                if mygas < 0:
                    i = i + j
                    flag = False
                    break
            if flag:
                return i
        return -1
            
        