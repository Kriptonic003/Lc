class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mx=max(candies)
        res=[]
        for i in range(len(candies)):
            sum=candies[i]+extraCandies
            if sum >= mx:
                res.append(True)
            else:
                res.append(False)
        return res            
        