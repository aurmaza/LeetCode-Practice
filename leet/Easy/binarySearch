class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l <=r:
            #Find middleof the array
            middle = l + (r - l) // 2  
            
            #If the middle number is the target return it
            if nums[middle] == target:
                return middle
            
            #If the middle number is less than the target cut left side of array
            elif nums[middle] < target:
                l = middle+1
            #If middle number is greater than target, cut right side of array off
            else:
                r = middle - 1
        #gone thru entire array w no match, return -1
        return -1
    