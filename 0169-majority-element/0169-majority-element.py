class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else :
                d[i]+=1
        for key,value  in d.items():
            if value == max(d.values()):
                return int(key)        
        