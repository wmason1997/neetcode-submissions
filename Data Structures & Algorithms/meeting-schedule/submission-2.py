"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        beginning, ending = 0, 1000000
        n = len(intervals)
        for i in range(n):
            if beginning <= intervals[i].start and intervals[i].end <= ending:
                beginning = intervals[i].end
            else:
                return False

        return True
