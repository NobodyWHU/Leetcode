class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        self.cost = cost
        self.gas = gas
        n = len(cost)
        for i in range(n):
            if self.helper(i):
                return i
        return -1
        
        
    def helper(self, start):
        new_gas = self.gas[start:]+self.gas[:start]
        new_cost = self.cost[start:]+self.cost[:start]
        left = 0
        for i in range(len(self.cost)):
            if left + new_gas[i] < new_cost[i]:
                return False
            left += new_gas[i] - new_cost[i]
        return True