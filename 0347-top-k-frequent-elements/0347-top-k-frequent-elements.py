class Solution:
    def topKFrequent(self, nums, k):
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        arr = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(arr[i][0])

        return ans