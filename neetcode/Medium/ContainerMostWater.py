class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        stored = 0
        while l < r:
            leftHeight = height[l]
            rightHeight = height[r]
            if leftHeight < rightHeight:
                currStored = (r-l) * leftHeight
                stored = max(stored,currStored)
                l += 1
            elif rightHeight < leftHeight:
                currStored = (r-l) * rightHeight
                stored = max(stored,currStored)
                r -= 1
            else:
                currStored = (r-l) * leftHeight
                stored = max(stored,currStored)
                l += 1
                r -= 1
        return stored