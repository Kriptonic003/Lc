class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ws=sum(nums[:k])
        ms=ws
        for i in range(k,len(nums)):
            ws=ws +nums[i] - nums[i-k]
            ms=max(ws,ms)
        return float(ms)/k    
        