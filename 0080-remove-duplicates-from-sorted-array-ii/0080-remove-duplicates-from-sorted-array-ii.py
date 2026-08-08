class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        prev=nums[0]
        count=1
        for i in range(1,len(nums)):
            if prev!=nums[i]:
                count=0   
            if (prev == nums[i] and count <2 )or prev != nums[i]:
                nums[k]=nums[i]
                k+=1
                prev=nums[i]
                count+=1
             
        return k
        