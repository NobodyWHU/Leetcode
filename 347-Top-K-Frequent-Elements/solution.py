class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        
        counter = Counter(nums)
        sorted_items = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        """
        we can use heapq
        heapq.nlargest(k, sorted_items, key=lambda x:c[x])
        """
        return [item[0] for item in sorted_items[:k]]
        