class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        searchWordLen = len(searchWord)
        words = sentence.split(" ")
        for i in range(len(words)):
            if len(words[i]) >= searchWordLen:
                if searchWord == words[i][0:searchWordLen]:
                    return i+1
        return -1
