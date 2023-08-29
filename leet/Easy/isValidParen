class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
     
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        if s[0] in pairs.values():
            return False
        for c in s:
       
            if c in pairs.keys():
                stack.append(c)
            elif stack:
                temp = stack.pop()
               
                if c != pairs[temp]:
                    print(c, pairs[temp])
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True
        
        
# gpt response
###
# Instead of using pairs.keys() and pairs.values(), you can directly check the membership in the dictionary, as this is more efficient.
# You don't need to check if len(s) == 1 at the beginning, as the main loop will handle this case correctly.
# You don't need to check if s[0] in pairs.values() at the beginning, as the main loop will handle this case correctly.
# You don't need to keep the temp variable; you can directly compare c with pairs[stack.pop()].
# You don't need to print(c, pairs[temp]).
# Instead of checking if len(stack) != 0 at the end, you can directly return not stack, which is equivalent and more readable.

###
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif stack and c == pairs[stack.pop()]:#checks if stack is empty and sees if the close paren matches the top of stack which is an open paren while also popping
                continue
            else:
                return False
        return not stack #If stack is empty, returns true
