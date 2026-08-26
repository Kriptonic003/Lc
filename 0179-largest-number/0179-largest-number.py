from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):

        def compare(a, b):
            a = str(a)
            b = str(b)

            if a + b > b + a:
                return -1
            else:
                return 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if compare(nums[i], nums[j]) == 1:
                    nums[i], nums[j] = nums[j], nums[i]
        if nums[0] == 0:
            return "0"            

        return ''.join(map(str, nums))