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

        nums = sorted(nums, key=cmp_to_key(compare))
        if nums[0] == 0:
            return "0"            

        return ''.join(map(str, nums))