class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        res = 0
        for n in text:
            if n in dic:
                dic[n] = dic[n] + 1
        
        minVal = min(list(dic.values()))
        while minVal > 0:
            for k, v in dic.items():
                if k == "l" or k == "o":
                    dic[k] = dic[k] - 2
                else:
                    dic[k] = dic[k] - 1
            minVal = min(list(dic.values()))
            if minVal >= 0:
                res+=1
        return res 
            
