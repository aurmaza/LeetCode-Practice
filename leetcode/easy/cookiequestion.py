class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        if not s:
            return res
        l,r = 0,0
        while r < len(s) and l < len(g):
            if g[l] <= s[r]:
               l+=1
               r+=1
               res+=1
            else:
                r +=1 
        return res
