class Solution:
    def process(self, st: str) -> str:
        stk = []
        for s in st:
            if s is not "#":
                stk.append(s)
            elif stk:
                stk.pop()
            else:
                continue
        return "".join(stk)


    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)
