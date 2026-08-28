class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        sr=0
        sc=0
        er=len(matrix)-1
        ec=len(matrix[0])-1
        ans=[]
        def printBound(a,sr,er,sc,ec):
            for j in range(sc,ec+1):
                ans.append(a[sr][j])
            for i in range(sr+1,er+1):
                ans.append(a[i][ec]) 
            if sr < er:    
                for j in range(ec-1,sc-1,-1):
                    ans.append(a[er][j])
            if sc<ec:        
                for i in range(er-1,sr,-1):
                    ans.append(a[i][sc])

        while sr<= er and sc<=ec:
            printBound(matrix,sr,er,sc,ec)
            sr+=1
            sc+=1
            ec-=1
            er-=1
        return ans    
        