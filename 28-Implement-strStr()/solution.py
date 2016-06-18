class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        len_s = len(haystack)
        len_t = len(needle)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1