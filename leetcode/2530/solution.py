import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert all elements to negative and push into a max heap (using Python's min heap)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            # Extract the largest element (most negative number)
            current_max = -heapq.heappop(max_heap)
            score += current_max
            # Push the updated value back into the heap
            heapq.heappush(max_heap, -(-current_max // 3))
        
        return score