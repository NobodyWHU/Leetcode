# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__intervals = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def upper_bound(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)/2
                if nums[mid].start > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        i = upper_bound(self.__intervals, val)
        start, end = val, val
        if i != 0 and self.__intervals[i-1].end+1 >= val:
            i -= 1
        while i!=len(self.__intervals) and end+1>=self.__intervals[i].start:
            start = min(start, self.__intervals[i].start)
            end  = max(end, self.__intervals[i].end)
            del self.__intervals[i]
        self.__intervals.insert(i, Interval(start, end))

        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.__intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()