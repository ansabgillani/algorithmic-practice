class Solution:
    def findMinDifference(self, timePoints):
        times = []
        for point in timePoints:
            hour, minute = map(int, point.split(':'))
            total_minutes = hour * 60 + minute
            times.append(total_minutes)
        
        times.sort()
        
        min_diff = (1440 - times[-1]) + times[0]
        
        for i in range(1, len(times)):
            diff = times[i] - times[i-1]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff