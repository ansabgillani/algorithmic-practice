class Solution:
    def countDaysWithoutMeetings(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start day
        meetings.sort()
        
        # Initialize the end of the previous meeting to 0
        prev_end = 0
        
        # Initialize available days counter
        available_days = 0
        
        for start, end in meetings:
            # Calculate the gap between the end of the previous meeting and the start of the current one
            available_days += max(0, start - prev_end - 1)
            
            # Update the end of the previous meeting to the maximum of its current value or the end of the current meeting
            prev_end = max(prev_end, end)
        
        # Add any remaining days after the last meeting
        available_days += max(0, days - prev_end)
        
        return available_days