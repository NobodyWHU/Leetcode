class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        while l < r:
            temp = numbers[l] + numbers[r]
            if temp > target:
                r -= 1
            elif temp < target:
                l += 1
            else:
                return [l+1, r+1]
        