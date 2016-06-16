class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for k, v in c1.items():
            if k not in c2:
                continue
            for _ in range(min(v,c2[k])):
                res.append(k)
        return res