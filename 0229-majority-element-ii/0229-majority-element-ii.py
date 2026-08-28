class Solution(object):
    def majorityElement(self, nums):

        d = {}
        ans = []

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in d:
            if d[i] > len(nums) / 3:
                ans.append(i)

        return ans