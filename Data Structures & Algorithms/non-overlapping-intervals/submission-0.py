class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        last_end = float('-inf')
        removals = 0
        for start, end in intervals:
            if start < last_end:
                # OVERLAP!
                removals += 1
            else:
                # No overlap, update the boundary
                last_end = end
        
        return removals