class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, nums):
        a=sorted(nums)
        if len(nums)==1:
            return 0
        mx=a[1]-a[0]
        for i in range(len(a)-1,1,-1):
            diff=a[i]-a[i-1]
            mx=max(mx,diff)
        return mx    
            
