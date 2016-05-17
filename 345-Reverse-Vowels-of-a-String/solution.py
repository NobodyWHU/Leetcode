class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = []
        index_rev = []
        vowles_list = ["a","e","i","o","u","A","E","I","O","U"]
        for index, i in enumerate(s):
            if i in vowles_list:
                rev.append(i)
                index_rev.append(index)
        
        s_list = list(s)
        index = 0
        while len(rev)>0:
            s_list[index_rev[index]] = rev.pop()
            index += 1
        return "".join(s_list)