class Solution:
    def createMap(self, words):
        d = {}
        for i, word in enumerate(words):
            d[word] = i
        return d
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = self.createMap(order)
        for i in range(0,len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:#Once encountering a difference in w1 w1, see if they are in correct order. If they are, break as they are in right place
                    if dic[word1[j]] > dic[word2[j]]:
                        print(word1[j], word2[j])
                        return False
                    break
            else:#This is hit if there are no breaks made by the for loop meaning w1 and w2 are equivalent up to max len word1, word2. If w1 is greater
            #than word2, w2 is a prefix of w1 and should be infront of w1.
                if len(word1) > len(word2):
                    return False

        return True
            
