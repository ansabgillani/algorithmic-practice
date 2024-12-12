import heapq
from math import sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert gifts into a min-heap by negating the values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        # Perform operations for k seconds
        for _ in range(k):
            # Extract the maximum value (negate back to original value)
            max_gift = -heapq.heappop(max_heap)
            # Reduce the gift count to the floor of its square root
            reduced_gift = int(sqrt(max_gift))
            # Push the reduced gift back into the heap (negated again)
            heapq.heappush(max_heap, -reduced_gift)
        
        # Calculate the total number of gifts remaining
        return -sum(max_heap)

# Test cases to verify the solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.pickGifts([25, 64, 9, 4, 100], 4))  # Output: 29
    print(sol.pickGifts([1, 1, 1, 1], 4))         # Output: 4