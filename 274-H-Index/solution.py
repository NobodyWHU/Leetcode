class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i, c in enumerate(sorted(citations, reverse=True)):
            if i >= c:
                return i
        return len(citations)