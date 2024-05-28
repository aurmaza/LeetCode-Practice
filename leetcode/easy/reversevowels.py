class Solution:
    def reverseVowels(self, s: str) -> str:        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        solved = ''
        vowlList = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowlList.append(s[i])
        vowlList.reverse()

        for i in range(len(s)):
            if s[i] in vowels:
                solved += vowlList[0]
                del vowlList[0]
            else:
                solved += s[i]
        return solved
            
