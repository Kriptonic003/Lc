class Solution(object):
    def longestCommonPrefix(self,strs):
        ans = ""

        shortest = strs[0]

        for i in range(len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        for i in range(len(shortest)):
            for j in strs:
                if j[i] != strs[0][i]:
                    return ans

            ans += strs[0][i]

        return ans
        