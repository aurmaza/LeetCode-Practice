class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        strs.sort(key=len)
        least = list(strs[0])
        for n in strs:
            nlist = list(n)
            leastLen = len(least)
            if not least:
                return ""
            for i in range(0, leastLen):    
                if least[i] != nlist[i]:
                    least = least[:i]
                    print(least)
                    break
        return ''.join(least)
