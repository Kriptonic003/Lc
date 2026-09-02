class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        seen=""
        mx=0
        for r in range(len(s)):
            while s[r] in seen:
                seen=seen[1:]
                l+=1
            seen+=s[r]
            mx=max(mx,r-l+1)  
        return mx      


