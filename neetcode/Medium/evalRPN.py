class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        #For each token t
        for t in tokens:
            if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
                stack.append(int(t))
            elif len(stack) > 1:
                element1 = stack.pop()
                element2 = stack.pop()
                res = 0
                if t == "+":
                    res = element1 + element2
                elif t =="*":
                    res = element1*element2
                elif t == "/":
                    if element2 * element1<0 and element2 % element1 != 0:
                        res = element2//element1 + 1
                    else: 
                        res = element2//element1
                else:
                    res = element2-element1
                stack.append(res)
        return stack[0]
