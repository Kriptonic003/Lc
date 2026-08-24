class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=[]
        s=s.split()
        for i in range(len(s)-1,-1,-1):
            r.append(s[i])
        return " ".join(r)    
        