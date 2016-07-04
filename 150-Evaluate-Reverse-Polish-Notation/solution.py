class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                s.append(int(t))
            else:
                
                two = s.pop()
                one = s.pop()
                if t == "+":
                    val = one + two
                elif t == "-":
                    val = one- two
                elif t == "*":
                    val = one * two
                else:
                    if one * two < 0:
                        val = -((-one)/two)
                    else:
                        val = one / two
                s.append(val)
        return s[0]