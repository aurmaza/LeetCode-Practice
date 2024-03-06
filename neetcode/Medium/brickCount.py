class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = { 0 : 0} #Position, gap count
        s = sum(wall[0])
        print(s)
        for row in wall:
            pos = 0
            for v in row[:-1]:#Don't include last brick as we dont want to count the end row.
                pos += v
                dic[pos] = 1 + dic.get(pos, 0)
        
        return len(wall) - max(dic.values())#Crossing most gaps=crossing least bricks.
