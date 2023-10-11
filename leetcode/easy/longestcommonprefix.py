class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        ['flow', 'flowers']
        #Can use the first string as a base since the smallest prefix would at moast be the size
        
        
        # of the smallest string
        for i in range(len(strs[0])):
            
            # For each string in strings
            for s in strs:
                
                # If the index is equal to the length of the string 
                #Means we will go out of bounds on string s
                #Return
                #Or if one of the strings doesnt match the first string 
                #return
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res