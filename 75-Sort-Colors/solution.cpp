class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        self.nums = nums
        zero_point, nonzero_point = 0,0
        while zero_point == n-1 or nonzero_point == n-1:
            while nums[zero_point] == 0:
                zero_point += 1
            while nums[nonzero_point] != 0:
                nonzero_pont += 1
            self.switch(zero_pont, nonzero_point)
        one_point, noone_point = zero_point+1, zero_point+1
        while one_point == n-1 or noone_point == n-1:
            while nums[one_point] == 1:
                one_point += 1
            while nums[noone_point] != 1:
                noone_point += 1
            self.switch(one_point, noone_point)
        
    def switch(self, a, b):
        temp = self.nums[a]
        self.nums[a] = self.nums[b]
        self.nums[b] = temp