class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        
        q, ans, vis = [s], [], set([s])
        found = False
        while q:
            cur = q.pop(0)
            if self.isValid(cur):
                found = True
                ans.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == "(" or cur[i]==")":
                        t = cur[:i]+cur[i+1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return ans
        
    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                if cnt==0:
                    return False
                cnt -= 1
        return cnt == 0