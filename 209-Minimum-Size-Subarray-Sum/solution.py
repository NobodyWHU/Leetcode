class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = total = 0
        n = len(nums)
        if n==0:
            return 0
        ans = n+1
        while right < n:
            while right<n and total < s:
                total += nums[right]
                right += 1
            if total < s:
                break
            while left < right and total >= s:
                total -= nums[left]
                left += 1
            ans = min(ans, right-left+1)
        if ans == n+1:
            return 0
        else:
            return ans