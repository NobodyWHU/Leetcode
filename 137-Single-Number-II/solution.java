class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if ((num>>i) & 1) == 1:
                    sum += 1
                    sum %= 3
            if sum != 0:
                ans = ans | (sum << i)
        
        return ans
        