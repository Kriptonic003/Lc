class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0
        
        for i in range(k):
            sum+=nums[i]
        mx=sum    
        for i in range(k,len(nums)):
            sum=sum+nums[i]-nums[i-k]
            mx=max(mx,sum)
        return float(mx)/k   

        