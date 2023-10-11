class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = [0] * len(nums)
        right = [0] * len(nums)

        #Nothing to left of nums[1], set to 1
        left[0] = 1
        
        #Nothing to right of nums[len(nums)-1], set to 1
        right[len(nums)-1] =1
        #Find all products of everything to left of nums[i]: 1 < i < =len(nums)
        for i in range(1,len(nums)):
            
            left[i] = left[i-1] * nums[i-1]
        #find all products of everything to left of nums[i] :0 <= i < len(nums)
            right[i] = right[i+1] * nums[i+1]
        print(left,right)
        res = []
        
        #Find product of everything left and right of each nums[i] for solution
        for i in range(0,len(nums)):
            res.append(left[i]*right[i])
        return res
            