import heapq

class Solution:
    def maxTwoEvents(self, events):
        # Sort events based on start time
        events.sort()
        
        # Initialize variables to store the best single event and overall result
        best_single = res = 0
        
        # Use a heap to keep track of end times and values of overlapping events
        heap = []
        
        for start, end, value in events:
            # Remove events that don't overlap with the current event from the heap
            while heap and heap[0][0] < start:
                _, prev_value = heapq.heappop(heap)
                best_single = max(best_single, prev_value)
            
            # Update the result with the maximum sum of non-overlapping values
            res = max(res, value + best_single)
            
            # Push the current event's end time and value into the heap
            heapq.heappush(heap, (end, value))
        
        return res