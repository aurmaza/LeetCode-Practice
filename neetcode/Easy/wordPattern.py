class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        print(s)
        for i,p in enumerate(pattern):
            if p in dic:
                if dic[p] != s[i]:
                    return False
                else:
                    continue
            else:
                if s[i] not in dic.values():
                    dic[p] = s[i]
                else:
                    #p not in dic, but si is in values already
                    return False
        return True
