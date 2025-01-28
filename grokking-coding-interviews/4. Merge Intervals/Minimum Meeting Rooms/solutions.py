from heapq import heappush, heappop

def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
        return 0
    
    # Sort the meetings by their start time
    intervals.sort(key=lambda x: x[0])
    
    # Min-heap to track the end times of meetings
    rooms = []
    heappush(rooms, intervals[0][1])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= rooms[0]:
            # If the next meeting starts after or when the earliest ending meeting ends,
            # reuse that room
            heappop(rooms)
        heappush(rooms, intervals[i][1])
    
    return len(rooms)

# Example usage:
# print(minMeetingRooms([[0,30],[5,10],[15,20]]))  # Output: 2
# print(minMeetingRooms([[7,10],[2,4]]))        # Output: 1