from heapq import heappop, heappush

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        
        # Initialize the heap with fractions formed by the smallest element and all other elements
        for j in range(1, n):
            heappush(min_heap, (arr[0] / arr[j], 0, j))
            
        # Extract the smallest fraction k-1 times to get to the k-th smallest fraction
        for _ in range(k - 1):
            frac, i, j = heappop(min_heap)
            if i + 1 < j:
                heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
        
        return [arr[i], arr[j]]