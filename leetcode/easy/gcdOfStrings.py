class Solution:
    def helper(self, q, subSmallest,smallest):
        for i in q:
            if i == subSmallest:
                continue
            else:
                return False
        if (len(smallest) % len(subSmallest)) !=0 :
            print(smallest,subSmallest)
            return False
        else:
            x = len(subSmallest)
            sArray = [smallest[i:i + x] for i in range(0, len(smallest), x)]
            for j in sArray:
                if j != subSmallest:
                    return False
        return True
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        larger = max(str1,str2)
        smaller = min(str1,str2)
        
        for i in range(len(smaller)):
            if (len(larger) % len(smaller)) == 0:
                x = len(smaller)
                q = [larger[p:p + x] for p in range(0, len(larger), x)]
                if self.helper(q,smaller, min(str1,str2)):
                    return smaller
            smaller = smaller[:-1]
        return smaller
           
