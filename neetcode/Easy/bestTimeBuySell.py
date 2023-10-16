class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP=0    
        l, r = 0,1
        while r < len(prices):
            if prices[l] <= prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxP