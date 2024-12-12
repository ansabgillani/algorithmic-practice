class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest_gift = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -math.isqrt(largest_gift))
            
        return -sum(max_heap)