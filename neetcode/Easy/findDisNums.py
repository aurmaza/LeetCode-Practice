def findDisappearedNumbers(nums):
    res = []
    for n in range(len(nums)):
        numAt = abs(nums[n]) - 1
        nums[numAt] = -1 * abs(nums[numAt])
        
    for n in range(len(nums)):
        if nums[n] < 0:
            res.append(n+1)
    


if __name__ == "__main__":
    findDisappearedNumbers([4,3,2,7,8,2,3,1])