class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []
        i = 0

        # Add all intervals before the overlapping interval(s)
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1

        result.append(newInterval)

        # Add all remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result