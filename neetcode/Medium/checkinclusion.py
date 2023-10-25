class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Counts = {}
        for char in s1:
            s1Counts[char] = s1Counts.get(char, 0) + 1
        l,r = 0,len(s1)-1
        while r < len(s2):
            tempArray = s2[l:r+1]
            tempDict={}
            for char in tempArray:
                tempDict[char] = tempDict.get(char, 0) + 1
            if s1Counts == tempDict:
                return True

            l+=1
            r+=1
        return False
  
#No creation of new dict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        # Initialize the s1 dictionary and the window dictionary
        s1Counts = {}
        windowCounts = {}
        for char in s1:
            s1Counts[char] = s1Counts.get(char, 0) + 1

        # Initialize the first window
        for char in s2[:len(s1)]:
            windowCounts[char] = windowCounts.get(char, 0) + 1

        if s1Counts == windowCounts:
            return True

        # Slide the window
        for i in range(1, len(s2) - len(s1) + 1):
            # Subtract one from the count of the leftmost character of the window
            left_char = s2[i - 1]
            windowCounts[left_char] -= 1
            if windowCounts[left_char] == 0:
                del windowCounts[left_char]

            # Add one to the count of the rightmost character of the new window
            right_char = s2[i + len(s1) - 1]
            windowCounts[right_char] = windowCounts.get(right_char, 0) + 1

            if s1Counts == windowCounts:
                return True

        return False
  
    