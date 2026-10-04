class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(prices)):
            f=1
            j=i+1
            while  j <len(prices):
                if prices[j]<=prices[i] :
                    res.append(prices[i]-prices[j])
                    f=0
                    break
                    
                else:
                    j+=1  
            if f==1:          
                res.append(prices[i])
        return res    

        