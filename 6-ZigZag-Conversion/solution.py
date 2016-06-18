class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        else:
            k=2*numRows-2
            l=len(s)
            sl=[]
            for i in range(l):
                sl.append(s[i])
            if k-l%k>0:
                for i in range(k-l%k):
                    sl.append(' ')
            l=len(sl)
            tr=[]
            for j in range(numRows):
                for i in range(l/k):
                    if j==0:
                        tr.append(sl[i*k])
                    elif j>0 and j<(numRows-1):
                        tr.append(sl[i*k+j])
                        tr.append(sl[(i+1)*k-j])
                    else:
                        tr.append(sl[i*k+numRows-1])

            return ''.join(tr).replace(' ','')