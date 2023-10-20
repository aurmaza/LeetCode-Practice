class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        maxlen = 0
        nums=set()
        for i, c in enumerate(s):
            print(nums, l, r)
            if c not in nums:
                nums.add(c)
                r+=1
                maxlen=max(maxlen,r-l)
            else:
                while c in nums:
                    nums.remove(s[l])
                    l+=1
                nums.add(c)
                r+=1
                maxlen = max(maxlen,r-l)   
        maxlen = max(maxlen, r-l)  
        return maxlen
        