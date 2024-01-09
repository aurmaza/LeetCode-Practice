class Solution:
    
    def getDict(self, s: str) -> dict:
        nDict = {}
        s = list(s)
        for i, c in enumerate(s):
            if c in nDict:
                continue
            else:
                nDict[c] = [i]
        return nDict
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = self.getDict(s)
        tDict = self.getDict(t)
        for c1, c2 in zip(s,t):
            sUniqueID = sDict[c1]
            tUniqueID = tDict[c2]
            if  sUniqueID != tUniqueID:
                return False
        return True            
