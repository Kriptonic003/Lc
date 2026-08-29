class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=[0]*len(height)
        left_max=0
        for i in range(len(height)):
            left_max=max(left_max,height[i])
            left[i]=left_max
        right=[0]*len(height)
        right_max=0
        for i in range(len(height)-1,-1,-1):
            right_max=max(right_max,height[i])
            right[i]=right_max 
        water=0    
        for i in range(len(height)):
            water+=min(right[i],left[i])-height[i]       

        return water