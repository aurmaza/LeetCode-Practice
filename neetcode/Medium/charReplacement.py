class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        count = {}
        res = 0
        

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1


            res = max(res, r-l+1)
        return res


# Fasterclass Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l,r = 0,0
        count = {}
        res = 0
        maxF = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])

            if (r-l+1) - maxF > k:
                count[s[l]] -=1
                l+=1
            res = max(res, r-l+1)

            r+=1
        return res


