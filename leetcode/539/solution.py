class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each time point to minutes since midnight
        times_in_minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        
        # Handle the circular nature of the clock by adding a day's worth of minutes at the end
        times_in_minutes.append(times_in_minutes[0] + 1440)
        
        # Calculate the minimum difference between consecutive times
        min_diff = min(b - a for a, b in zip(times_in_minutes, times_in_minutes[1:]))
        
        return min_diff

# Example usage:
sol = Solution()
print(sol.findMinDifference(["23:59", "00:00"]))  # Output: 1
print(sol.findMinDifference(["00:00", "23:59", "00:00"]))  # Output: 0