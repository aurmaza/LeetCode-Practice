class Solution:
    def toDict(self, st):
        dic = {}
        for s in st:
            dic[s] = 1 + dic.get(s, 0)
        return dic
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rDict = self.toDict(ransomNote)
        mDict = self.toDict(magazine)

        for k in rDict.keys():
            if k not in mDict.keys():
                return False
            if rDict[k] > mDict[k]:
                return False
        return True
        
