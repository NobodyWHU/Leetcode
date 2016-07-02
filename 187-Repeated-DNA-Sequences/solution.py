class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        one = set()
        repeat = set()
        for i in range(len(s)-9):
            ten = s[i:i+10]
            if ten in one:
                repeat.add(ten)
            else:
                one.add(ten)
        return list(repeat)