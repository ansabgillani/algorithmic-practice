from heapq import heappush, heappop

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Sort by arrival time and then by leaving time in case of a tie
        events = sorted([(t[0], t[1], i) for i, t in enumerate(times)])
        
        # Min heap to keep track of available chairs
        available_chairs = []
        # Min heap to keep track of occupied chairs with the time they become free
        occupied_chairs = []
        
        for arrival, leaving, friend in events:
            # Free up chairs that are now available
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                heappush(available_chairs, heappop(occupied_chairs)[1])
            
            if friend == targetFriend:
                return available_chairs[0] if available_chairs else len(available_chairs)
            
            # Assign the smallest available chair
            if available_chairs:
                heappush(occupied_chairs, (leaving, heappop(available_chairs)))
            else:
                heappush(occupied_chairs, (leaving, len(available_chairs)))
                heappush(available_chairs, len(available_chairs))
        
        return -1  # This should never happen given the problem constraints