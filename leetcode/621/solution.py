from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        # Create a max heap based on task frequencies
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while max_heap:
            # Extract the most frequent tasks
            current_batch = []
            for _ in range(n + 1):
                if max_heap:
                    current_batch.append(-heapq.heappop(max_heap))
                
            # Decrease the frequency and push back into heap if not done completely
            for count in current_batch:
                if count > 1:
                    heapq.heappush(max_heap, -(count - 1))
            
            # Increment time by (n+1) or number of tasks processed in this batch
            time += n + 1 if max_heap else len(current_batch)
        
        return time