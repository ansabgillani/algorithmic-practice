import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # Initialize a min-heap to keep track of the k largest elements seen so far.
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the heap if it's smaller than the current smallest element in the heap (kth largest).
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        # The root of the min-heap is always the kth largest element.
        return self.heap[0]