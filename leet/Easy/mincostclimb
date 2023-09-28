class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # [10,15,20] 0
        cost.append(0)
        #Len cost -3 as we dont need to evaluate the last index or the 0 index

        
        for i in range(len(cost) - 3, -1, -1):
            oneStep = cost[i] + cost[i+1]
            twoStep = cost[i] + cost[i+2]
            cost[i] = min(oneStep, twoStep)
        return min(cost[0], cost[1])
