class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        ans = []

        for start, end in intervals:

            if not ans:
                ans.append([start,end])
            elif start<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],end)
            else:
                ans.append([start,end])
        return ans    

        