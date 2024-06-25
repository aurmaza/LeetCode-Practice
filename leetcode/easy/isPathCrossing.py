class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        curr = (0,0)

        for i in path:
            print(i,visited)
            move = curr
            if i == 'N':
                move = (move[0], move[1] +1)
            elif i == 'S':
                move = (move[0], move[1] -1) 
            elif i == 'E':
                move = (move[0]+1,move[1])
            else:
                move= (move[0]-1, move[1])
            
            if move in visited:
                return True
            else:
                curr=move
                visited.add(move)
                
        return False
