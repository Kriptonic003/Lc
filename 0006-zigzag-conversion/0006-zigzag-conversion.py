class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:return s
        d=1
        i=0
        rows=[[] for _ in range(numRows)]
        for ch in s:
            rows[i].append(ch)
            if i==0:
                d=1
            if i == numRows-1:
                d=-1
            i+=d
        ret=""
        for i in range(numRows):
            ret += "".join(rows[i])            
        return ret