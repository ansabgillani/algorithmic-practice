from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap to keep track of available rooms (room number)
        available = list(range(n))
        heapq.heapify(available)
        
        # Min-heap to keep track of occupied rooms (end_time, room_number)
        occupied = []
        
        # Count the number of meetings each room has held
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have ended their meeting by start time
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            if available:
                # Assign the lowest numbered available room
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
                count[room] += 1
            else:
                # Delay the meeting in the earliest ending occupied room
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (end_time + (end - start), room))
                count[room] += 1
        
        # Find the room with the most meetings
        return count.index(max(count))

# Example usage:
sol = Solution()
print(sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # Output: 0
print(sol.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))  # Output: 1