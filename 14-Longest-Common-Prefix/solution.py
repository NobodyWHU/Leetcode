class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        minLength = len(strs[0])
        index = 0
        for i in range(1,len(strs)):
            if len(strs[i]) < minLength:
                minLength = len(strs[i])
                index = i
        shortest_str = strs[index]
        count_list = [0 for i in range(len(shortest_str))]
        for i in range(minLength):
            for j in range(len(strs)):
                if strs[j][i] == shortest_str[i]:
                    count_list[i] += 1
        prefix = ""
        for i in range(minLength):
            if count_list[i] == len(strs):
                prefix += shortest_str[i]
            else:
                break
        return prefix
        