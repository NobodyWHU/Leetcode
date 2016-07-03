class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","")
        val_list = []
        operator_list = []
        temp = []
        for c in s:
            if c.isdigit():
                temp.append(c)
                continue
            else:
                val_list.append(int("".join(temp)))
                temp = []
                operator_list.append(c)
        if len(temp) != 0:
            val_list.append(int("".join(temp)))
        
        i = 0
        while i < len(operator_list):
            if operator_list[i] == "*":
                val_list[i] = val_list[i] * val_list[i+1]
                val_list.pop(i+1)
                operator_list.pop(i)
            elif operator_list[i] == "/":
                val_list[i] = val_list[i] / val_list[i+1]
                val_list.pop(i+1)
                operator_list.pop(i)
            else:
                i += 1
        
        i = 0
        while i < len(operator_list):
            if operator_list[i] == "+":
                val_list[i] = val_list[i] + val_list[i+1]
                val_list.pop(i+1)
                operator_list.pop(i)
            else:
                val_list[i] = val_list[i] - val_list[i+1]
                val_list.pop(i+1)
                operator_list.pop(i)
        
        return val_list[0]
                