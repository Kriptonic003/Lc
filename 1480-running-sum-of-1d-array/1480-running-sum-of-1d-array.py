class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=nums[0]
        r=[sum]
        for i in range(1,len(nums)):
            sum=sum+nums[i]
            r.append(sum)
            
        return r