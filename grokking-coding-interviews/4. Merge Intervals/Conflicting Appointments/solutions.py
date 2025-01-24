class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by start time
        intervals.sort()
        
        # Check if there is any overlap between consecutive meetings
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True

# Test cases
print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))  # Output: False
print(Solution().canAttendMeetings([[7,10],[2,4]]))          # Output: True