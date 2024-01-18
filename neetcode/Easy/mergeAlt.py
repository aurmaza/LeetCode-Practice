class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = len(word1), len(word2)
        smallerWord = min(p1,p2)
        word1 = list(word1)
        word2 = list(word2)
        i = 0
        res = ""
        while i < smallerWord:
            res+=word1.pop(0)
            res+=word2.pop(0)
            i+=1
        if word1:
            while word1:
                res+= word1.pop(0)
        if word2:
            while word2:
                res+= word2.pop(0)
        
        return ''.join(res)
        
