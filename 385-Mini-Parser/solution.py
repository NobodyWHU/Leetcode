# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        parsed, _ = self.helper(s, 0)
        return parsed
        
        
    def helper(self, s, ind):
        i = ind
        # scenario 1: to parse a nested list
        if s[i] == '[':
            parsed = NestedInteger()
            i += 1
            while i < len(s):
                if s[i] == ']':
                    return parsed, i+1
                if s[i] == '[':
                    nested, i = self.helper(s, i)
                    parsed.add(nested)
                elif s[i] in '-0123456789':
                    ele, i = self.helper(s, i)
                    parsed.add(ele)
               # put this case at the bottom so that we don't need list all the spaces (e.g. space, tab) or comma separator
                else:
                    i += 1
       # scenario 2: to parse an integer
        else:
            temp = i
            while temp < len(s) and s[temp] in '-0123456789':
                temp += 1
            return NestedInteger(int(s[i:temp])), temp
        