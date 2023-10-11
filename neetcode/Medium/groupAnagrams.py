# mySolution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for s in strs:
            sortStr = ''.join(sorted(s))
            if sortStr not in dictionary.keys():
                dictionary[sortStr] = [s]
            else:
                dictionary[sortStr].append(s)
        return dictionary.values()
    