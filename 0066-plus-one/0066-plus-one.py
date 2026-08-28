class Solution(object):
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, digits):
        a="".join(map(str,digits))
        ans=str(int(a)+1)
        ans=list(ans)
        return map(int,ans)
        