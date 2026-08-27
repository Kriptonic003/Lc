class Solution(object):
    def firstMissingPositive(self, nums):
        d = {}

        for n in nums:
            if n > 0 and n <= len(nums):
                d[n] = True

        for i in range(1, len(nums) + 1):
            if i not in d:
                return i

        return len(nums) + 1