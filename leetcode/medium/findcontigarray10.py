class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = 0
        dic = {0:-1}
        count = 0
        for i,n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in dic: m = max(m, i - dic[count])
            else: dic[count] = i
        return m
#Keep a dict that holds the first index where each unique 'count' value was encountered
#if the same count is seen again, the dict help us find start of the subarray that balances 0 and 1 
#to the curr index
#so its the distance between that index and the current index
# if we encounter a count that already exists, that means
#from where it is first encountered to the current
#it has been rebalanced and the subarray from curr to index of the first encounter is balanced
