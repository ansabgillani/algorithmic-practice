class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a list of non-overlapping intervals and merges overlapping intervals.
        
        :param intervals: List of sorted non-overlapping intervals.
        :type intervals: List[List[int]]
        :param newInterval: New interval to insert.
        :type newInterval: List[int]
        :return: Merged list of intervals after insertion.
        :rtype: List[List[int]]
        """
        result = []
        i, n = 0, len(intervals)
        
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        result.append(newInterval)
        
        # Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.insert([[1,3],[6,9]], [2,5]))  # Output: [[1,5],[6,9]]
print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]