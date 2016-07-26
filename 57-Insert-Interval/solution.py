# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        isInsert = False
        n = len(intervals)
        ret = []
        for inter in intervals:
            if isInsert:
                ret.append(inter)
                continue
            if newInterval.end < inter.start:
                ret.append(newInterval)
                ret.append(inter)
                isInsert = True
                continue
            
            if newInterval.start <= inter.end and inter.start <= newInterval.end:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end = max(newInterval.end, inter.end)
                continue
            ret.append(inter)
        if not isInsert:
            ret.append(newInterval)
        return ret