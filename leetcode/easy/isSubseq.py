class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stk = list(s)
        t = list(t)
        for c in t:
            if stk and c == stk[0]:
                stk.pop(0)
          
        return not stk
      
