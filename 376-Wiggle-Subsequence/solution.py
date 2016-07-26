class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        size = len(nums)
        inc, dec = [1] * size, [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    inc[x] = max(inc[x], dec[y] + 1)
                elif nums[x] < nums[y]:
                    dec[x] = max(dec[x], inc[y] + 1)
        return max(inc + dec) if size else 0