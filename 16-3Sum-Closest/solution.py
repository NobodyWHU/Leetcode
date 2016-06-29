class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        ans = None
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                sum = nums[i]+nums[r]+nums[l]
                if ans is None or abs(sum-target)<abs(ans-target):
                    ans = sum
                if sum <= target:
                    l += 1
                else:
                    r -= 1
        return ans