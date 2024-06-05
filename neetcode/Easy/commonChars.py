class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordSet = {}
        for w in words[0]:
                wordSet[w] = wordSet.get(w,0) + 1
        for i in range(1,len(words)):
            temp = {}
            for w in words[i]:
                temp[w] = temp.get(w,0)+1
            for w in list(wordSet):
                print(temp, wordSet)
                if w in temp:
                    if temp[w] >= wordSet[w]:
                        continue
                    else:
                        wordSet[w] = temp[w]
                else:
                    del wordSet[w]
        res = []
        print(wordSet)
        for m in wordSet:
            n = wordSet[m]
            for k in range(0,n):
                res.append(m)
        return res

        
            
            
