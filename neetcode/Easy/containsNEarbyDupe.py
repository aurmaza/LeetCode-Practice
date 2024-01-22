class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic:
                dic[v].append(i)
            else:
                dic[v] = [i]
        print(dic)
        for v in dic.values():
            if len(v) >= 2:
                m = float('inf')
                for d in range(1,len(v)):
                    m = min(m, abs(v[d]-v[d-1]))
                if m <= k:
                    return True                    
            
            
        return False
