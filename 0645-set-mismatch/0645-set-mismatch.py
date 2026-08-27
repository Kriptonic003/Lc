class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mx=max(nums)
        mn=min(nums)
        s=set(nums)
        # for i in range(len(nums)):
        #     if nums.count(nums[i])>1:
        #         dup=nums[i]
        #         break
        seen = set()

        for n in nums:
            if n  in seen:
                dup = n
                break
            seen.add(n)
        for i in range(1,mx+1):
            if i not in s:
                return [dup,i] 
        return [dup,len(nums)]