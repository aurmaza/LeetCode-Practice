class Solution(object):
    
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for num in range(0, n + 1, 1):
            binnum = bin(num).count('1')
            
            res.append(binnum)
        return res

            
dumb way to do it ^

smart way

class Solution(object):
    
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n+1)
        
        offset =1 
        for num in range(1, n+1):
            if offset * 2 == num:
                offset = num
            res[num] = 1 + res[num-offset]

            
                        
        return res

            