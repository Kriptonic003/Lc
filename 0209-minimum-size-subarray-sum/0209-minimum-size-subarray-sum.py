class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        cur=0
        mn=float('inf')
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>=target:
                ln=r-l+1
                mn=min(mn,ln)
                cur-=nums[l]
                l+=1
        if mn == float('inf'):
            return 0

        return mn