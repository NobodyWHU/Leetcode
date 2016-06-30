class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = {}
        if not strs:
            return []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in temp:
                temp[sorted_s] = [s]
            else:
                temp[sorted_s].append(s)
        
        ans = []
        for v in temp.values():
            ans.append(v)
        return ans