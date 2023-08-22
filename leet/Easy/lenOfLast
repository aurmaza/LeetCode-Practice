class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split(" ")
        newtemp = list(filter(lambda x: len(x) >= 1, temp))
        print(newtemp)
        return len(newtemp[len(newtemp)-1])
##neet code

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index, length = len(s) - 1, 0
        while s[index] == " ":
            index -= 1
        while s[index] != " " and index>=0:
            length += 1
            index -=1
        return length
        

        