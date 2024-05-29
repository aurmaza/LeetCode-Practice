
def convertToTitle( columnNumber):
    res = ""
    while columnNumber>0:
        offset = (columnNumber - 1) % 26 #Find the offset from A.  A i
        print(ord('A'), chr(offset))
        res +=chr(ord('A') + offset)
        columnNumber = (columnNumber-1 )// 26
    return res[::-1]


convertToTitle(542)