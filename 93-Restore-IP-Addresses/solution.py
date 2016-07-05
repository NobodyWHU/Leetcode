class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(s, 0, "", ans)
        return ans
    
    def dfs(self, s, sub, ip, ans):
        if sub == 4:
            if s == "":
                ans.append(ip[1:])
            return
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], sub+1, ip+"."+s[:i], ans)
                if s[0] == "0":
                    break
            
        
        