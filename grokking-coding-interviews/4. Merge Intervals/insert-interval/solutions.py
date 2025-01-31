class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into the list of non-overlapping intervals and merges overlapping intervals.
        
        :param intervals: List of non-overlapping intervals sorted by start time.
        :type intervals: List[List[int]]
        :param newInterval: Interval to be inserted.
        :type newInterval: List[int]
        :return: Merged list of non-overlapping intervals.
        :rtype: List[List[int]]
        """
        
        result = []
        i, n = 0, len(intervals)
        
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        result.append(newInterval)
        
        # Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result