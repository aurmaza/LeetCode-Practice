class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for o in operations:
            print(score)
            if o.lstrip('-').isnumeric():
                score.append(int(o))
            else:
                if o == '+':
                    score.append(score[-1] + score[-2])
                elif o == 'D':
                    score.append(score[-1] * 2)
                elif o == 'C':
                    score.pop()
        
        return sum(score)
