from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # Priority queue to keep track of the end times of groups
        end_times = []
        
        for interval in intervals:
            if end_times and interval[0] > end_times[0]:
                # If the current interval starts after or when the earliest ending group ends,
                # reuse that group
                heapq.heapreplace(end_times, interval[1])
            else:
                # Otherwise, start a new group
                heapq.heappush(end_times, interval[1])
        
        # The number of groups needed is the size of the priority queue
        return len(end_times)