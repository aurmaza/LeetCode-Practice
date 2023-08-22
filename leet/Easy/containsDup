class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False
        count = 0
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        print(countS,countT)
        for j in countT:
            if countT.get(j) != countS.get(j,0):
                return False
        return True

# 