class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mx=0
        mn=float('inf')
        for i in range(len(prices)):
            
            req=prices[i]-mn
            if req > mx:
                mx= req
            if prices[i]<mn:
                mn=prices[i]    
                
        return mx            