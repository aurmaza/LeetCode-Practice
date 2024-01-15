class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)
        while r <= len(haystack):
            subString = haystack[l:r]
            if subString == needle:
                return l
            l+=1
            r+=1
        return -1
