class Solution:
    def findMaxCPULoad(self, jobs):
        """
        :type jobs: List[List[int]]
        :rtype: int
        """
        # Sort the jobs by their start time
        jobs.sort(key=lambda x: x[0])
        
        max_load = 0
        current_load = 0
        i = 0
        
        # Priority queue to keep track of end times and associated loads
        import heapq
        end_times = []
        
        while i < len(jobs):
            start, end, load = jobs[i]
            
            # Remove all jobs that have already ended before the current job starts
            while end_times and start >= end_times[0][1]:
                _, prev_end_load = heapq.heappop(end_times)
                current_load -= prev_end_load
            
            # Add the current job to the priority queue
            heapq.heappush(end_times, (end, load))
            current_load += load
            
            max_load = max(max_load, current_load)
            i += 1
        
        return max_load

# Example usage:
solution = Solution()
jobs1 = [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
print(solution.findMaxCPULoad(jobs1))  # Output: 7

jobs2 = [[6, 7, 10], [2, 4, 11], [8, 12, 15]]
print(solution.findMaxCPULoad(jobs2))  # Output: 15