class Solution:
    def intersect(self, nums1, nums2):
        d = {}

        for num in nums1:
            d[num] = d.get(num, 0) + 1

        ans = []

        for num in nums2:
            if d.get(num, 0) > 0:
                ans.append(num)
                d[num] -= 1

        return ans