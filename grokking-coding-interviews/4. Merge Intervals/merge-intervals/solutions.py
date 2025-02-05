class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            if current[0] <= last_merged[1]:
                # There is an overlap, so merge them
                merged[-1][1] = max(last_merged[1], current[1])
            else:
                # No overlap, add the current interval to the merged list
                merged.append(current)
        
        return merged