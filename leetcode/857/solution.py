import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        ans = float('inf')
        total_quality = 0
        heap = []
        
        for ratio, q in workers:
            total_quality += q
            heapq.heappush(heap, -q)
            
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
                
            if len(heap) == k:
                ans = min(ans, total_quality * ratio)
                
        return ans