class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospaces = s.lower().replace(" ", "")
        noalnum = "".join(char for char in nospaces if char.isalnum())
        reverseText = noalnum[::-1]
        print(noalnum, reverseText)
        return noalnum == reverseText
    
class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.alphaNum(s[l]):
                l+=1
            while r > l and not self.alphaNum(s[r]):
                r-=1
            print(l,r)
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True



    def alphaNum(self, c):
        # ord takes in only string

        return (ord('A') <= ord(c) <= ord('Z') or
                 ord('a') <= ord(c) <= ord('z') or
                 ord('0') <= ord(c) <= ord('9'))
