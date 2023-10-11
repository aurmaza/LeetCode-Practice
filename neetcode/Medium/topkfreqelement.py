class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dictionary = {}
        for i in nums:
            if i not in dictionary.keys():
                dictionary[i] = 1
            else:
                dictionary[i] += 1
  
        arr = [[] for i in range(0,len(nums)+1)]
   
        # for key in dictionary.keys():
        #     arr[dictionary[key]].append(key)
        
        #BIG ISSUE
        #Code was messing up as i had 
        # for k, v in dictionary.items();
        #And it would set k to for example 3
        #then in the check at bottom len(res) == k would end at 3
        #Or whatever key value was last in dictionar.items()
    


        for c, v in dictionary.items():
            arr[v].append(c)
        res = []
        print(arr)
        for t in range(len(arr)-1, -1, -1):
            for n in arr[t]:
                res.append(n)
                if len(res) == k:
                    print(len(res), k)
                    return res

                
                
            