class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        mySet = set()
        originalnum = n
        mySet.add(n)
        status = True
        while status:
            if originalnum == 1:
                return True
            numString = [int(d) for d in str(originalnum)]

            squared = [v**2 for v in numString]
            numsum = sum(squared)
            if numsum in mySet:
                return False
            mySet.add(numsum)
            originalnum = numsum
            
            



    