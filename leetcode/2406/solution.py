import heapq

class Solution:
    def minGroups(self, intervals):
        intervals.sort(key=lambda x: x[0])
        end_times = []
        
        for interval in intervals:
            if end_times and end_times[0] < interval[0]:
                heapq.heapreplace(end_times, interval[1])
            else:
                heapq.heappush(end_times, interval[1])
        
        return len(end_times)