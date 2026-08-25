class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels="aeiouAEIOU"
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        mx=count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            mx=max(count,mx)
        return mx                    
        