class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c=sorted(citations)
        for i in range(len(c)):
            if c[i]>=len(c)-i:
                return len(c)-i
        return 0        

        