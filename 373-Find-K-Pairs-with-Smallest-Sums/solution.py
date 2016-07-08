import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) * len(nums2) <= k:
            return [[i, j] for i in nums1 for j in nums2]
        
        hp = [[n + nums2[0], n, 0] for n in nums1]
        res = []
        for i in range(k):
            psum, n, ind = hp[0]
            res.append([n, psum-n])
            if ind + 1 == len(nums2):
                heapq.heappop(hp)
            else:
                heapq.heapreplace(hp, [n + nums2[ind+1], n, ind+1])
        return res