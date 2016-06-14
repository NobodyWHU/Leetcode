class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + flag == 10:
                flag = 1
                digits[i] = 0
            else:
                
                digits[i] = digits[i] + flag
                flag = 0
        if flag == 1:
            digits.insert(0, 1)
        return digits
        