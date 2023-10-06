class Solution(object):
    def moveRobot(self, letter, robotPos):
        x, y, directions = robotPos
        mv = {
            'N' : (0,1),
            'S' : (0,-1),
            'E' : (1, 0),
            'W' : (-1, 0)
        }
        left ={
            'N' : 'W',
            'S' : 'E',
            'E' : 'N',
            'W' : 'S'
        }
        right ={
            'N' :'E',
            'S' : 'W',
            'E' : 'S',
            'W' : 'N'
        }
        if letter == 'G':
            i,j = mv[directions]
            x+= i
            y+= j
        if letter == 'L':
            directions = left[directions]
        if letter == 'R':
            directions = right[directions]
        return [x,y,directions]
    def isOrigin(self, array):
        if array[0] == 0 and array[1] == 0:
            return True
        return False
    def isRobotBounded(self, instructions):
        '''
        :type instructions: str
        :rtype: bool
        '''

        robotPosition = [0, 0,'N']
        for ins in instructions:
            print(robotPosition)
            robotPosition = self.moveRobot(ins, robotPosition)
        if self.isOrigin(robotPosition) or robotPosition[2] != 'N':
            return True
        print(robotPosition)
        return False



        