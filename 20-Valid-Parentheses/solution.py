class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {']' : '[', '}' : '{', ')' : '('}
        stack = []
        for char in s:
            if char in dic.viewvalues():
                stack.append(char)
            elif char in dic:
                if not stack or stack.pop() != dic[char]:
                    return False
        return True if not stack else False
                    