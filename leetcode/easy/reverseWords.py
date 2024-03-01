class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        temp = ''
        for c in s:
            if c is not " ":
                temp = c + temp
            else:
                res = res + temp + ' '
                temp = ''
        if temp:
            res += temp
        return res
