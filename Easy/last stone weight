class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones) 
        print(stones)

        while len(stones) > 1:
           largest =  heapq.heappop(stones)
           secondlargest = heapq.heappop(stones)
           if largest == secondlargest:
               continue
           else:
               temp = -1 * (secondlargest - largest)
               heapq.heappush(stones, temp)
        
        if len(stones) is 0:
            return 0
        print(stones)
        return abs(stones[0])
        

        return stones