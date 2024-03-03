class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pSorted = sorted(pairs, key=lambda x : x[1])
        chainLen = 1
        
   
        currEndValue = pSorted[0][1]
        # print(pSorted)
        for i in range(1, len(pSorted)):
            if pSorted[i][0] > currEndValue:
                currEndValue = pSorted[i][1]
                chainLen+=1
             
        return chainLen
