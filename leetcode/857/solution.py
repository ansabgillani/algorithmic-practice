class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate the ratio of wage to quality for each worker and sort by this ratio
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        
        total_quality = 0
        max_heap = []
        min_cost = float('inf')
        
        for ratio, q in workers:
            # Add the current worker's quality to the total quality
            total_quality += q
            heapq.heappush(max_heap, -q)
            
            # If we have more than k workers, remove the one with the highest quality
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            
            # When we have exactly k workers, calculate the cost
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        
        return min_cost