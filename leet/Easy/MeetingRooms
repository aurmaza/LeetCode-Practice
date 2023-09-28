class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        def getFirst(data: Interval):
            return data.start

        intervals.sort(key=getFirst)

        for i in range(0, len(intervals)-2):
            if(intervals[i].end >= intervals[i+1].start):
                return False
        return True
