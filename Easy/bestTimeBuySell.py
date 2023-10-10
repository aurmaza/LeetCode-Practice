class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: return 0
        if len(prices) == 2:
            temp = prices[1] - prices[0]
            if(temp > 0):
                return temp
            else:
                return 0
        ///
        
        maxP=0    
        l, r = 0, 1
        while r < len(prices):
            # If left price is less than right
            #Profit is possible
            #Don't increment left pointer
            if prices[l] < prices[r]:
                maxP=max(maxP,prices[r]-prices[l])
            #Profit is not possible, move the left pointer to where right pointer is
            else:
                l=r
            #Increment right pointer regardless
            r+=1
        return maxP