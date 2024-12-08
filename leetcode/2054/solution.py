import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        
        # Extract end times and values to use with binary search
        end_times = [event[1] for event in events]
        values = [event[2] for event in events]
        
        # Initialize the maximum value found so far
        max_value_so_far = 0
        
        # Array to store the maximum value up to each index (end time)
        max_values_up_to = [0] * len(events)
        
        # Fill the array with the maximum values up to each end time
        for i in range(len(events)):
            max_values_up_to[i] = max(max_value_so_far, values[i])
            if i > 0:
                max_values_up_to[i] = max(max_values_up_to[i], max_values_up_to[i-1])
            max_value_so_far = max(max_value_so_far, values[i])
        
        # Result to store the maximum sum of two non-overlapping events
        result = 0
        
        # Iterate through each event and find the best non-overlapping event after it
        for i in range(len(events)):
            end_time = events[i][1]
            index = bisect.bisect_left(end_times, end_time + 1)
            if index < len(events):
                result = max(result, values[i] + max_values_up_to[index])
        
        return result