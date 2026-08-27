# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        for start,end in intervals:

            if not ans:
                ans.append([start,end])
            elif start<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],end)
            else:
                ans.append([start,end])
        return ans
