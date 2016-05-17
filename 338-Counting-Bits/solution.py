class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1,num+1):
            if i%2==0:
                res[i] = res[i/2]
            else:
                res[i] = res[i/2]+1

        return res        