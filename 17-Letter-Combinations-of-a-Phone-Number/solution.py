class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        length = len(digits)
        if length == 0:
            return []
        ans =[]
        def dfs(num, temp, length, ans):
            if num == length:
                ans.append(temp)
                return
            for i in dict[digits[num]]:
                dfs(num+1, temp+i, length, ans)
        
        dfs(0, "", length, ans)
        return ans