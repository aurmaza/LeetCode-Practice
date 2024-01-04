class Solution:
    def romanToInt(self, s: str) -> int:
        listWords = list(s)
        
        symVals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        nextVal = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD' : 400,
            'CM' : 900
        }
        
        others = ['I', 'C', 'X']
        sumNums = 0
        i = 0
        while i < len(listWords):
            if listWords[i] in others and i is not len(listWords)-1:
                if (listWords[i]+listWords[i+1]) in nextVal:
                    sumNums += nextVal[listWords[i] + listWords[i+1]]
                    print(nextVal[listWords[i] + listWords[i+1]])
                    i+=1
                else:
                    sumNums += symVals[listWords[i]]
                    print(symVals[listWords[i]])
            else:
                sumNums += symVals[listWords[i]]
                print(symVals[listWords[i]])
            i+=1
        return sumNums