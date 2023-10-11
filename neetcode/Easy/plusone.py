class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(v) for v in digits]
        i = int("".join(s))
        i = i + 1
        t = str(i)
        return [int(j) for j in t]