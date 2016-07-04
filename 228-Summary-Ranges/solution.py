class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start = end = nums[0]
        ans = []
        for i, num in enumerate(nums[1:]):
            if end + 1 == num:
                end = num
            else:
                if end == start:
                    ans.append(str(start))
                else:
                    ans.append("%s->%s" % (start, end))
                start = end = num
        if end == start:
            ans.append(str(start))
        else:
            ans.append("%s->%s" % (start, end))
        return ans