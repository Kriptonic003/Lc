class Solution(object):
    def strStr(self, haystack, needle):

        if needle == "":
            return 0

        l = 0
        r = 0

        while l < len(haystack):

            if haystack[l] == needle[r]:

                start = l

                while r < len(needle):

                    if l >= len(haystack) or haystack[l] != needle[r]:
                        l = start + 1
                        r = 0
                        break

                    l += 1
                    r += 1

                if r == len(needle):
                    return start

            else:
                l += 1

        return -1