class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        minL = min(len(v1), len(v2))
        for i in range(minL):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
        if len(v1) > minL:
            for t in v1[minL:]:
                if int(t) > 0:
                    return 1
            return 0
        elif len(v2) > minL:
            for t in v2[minL:]:
                if int(t) > 0:
                    return -1
            return 0
        else:
            return 0