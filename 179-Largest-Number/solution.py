class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(nums, cmp=lambda x, y:1 if str(x)+str(y)<str(y)+str(y) else -1)
        largest = "".join(str(i) for i in nums)
        i, n = 0, len(largest)
        while i+1 < n:
            if largest[i] != "0":
                break
            i += 1
        return largest[i:]