class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>prev:
                ans+=(prices[i]-prev)
            prev=prices[i]
        return ans    

        