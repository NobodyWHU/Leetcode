class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        i, j = 0, len(citations)-1
        N = len(citations)
        while i <= j:
            mid = (i+j)/2
            if N-mid > citations[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return N-i