class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l=[]
        r=[]
        for i in range(n):
            l.append(nums[i])
        for i in range(n,len(nums)):
            r.append(nums[i])
            res=[]    
        for i in range(n):
            if l[i]:
                res.append(l[i])
            if r[i]:
                res.append(r[i])     
        return res        