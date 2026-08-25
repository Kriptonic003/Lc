class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        cur=[]
        for i in range(rowIndex):
            cur=[1]
            for j in range(1,len(row)):
                cur.append(row[j-1]+row[j])
            cur.append(1)
            row = cur
        return row        
        