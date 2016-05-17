class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(nums)
        sorted_items = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
        