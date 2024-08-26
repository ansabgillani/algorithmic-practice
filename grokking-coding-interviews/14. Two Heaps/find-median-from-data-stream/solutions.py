import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # Max-heap to store the smaller half of the numbers
        self.large = []  # Min-heap to store the larger half of the numbers

    def addNum(self, num: int) -> None:
        # Push number into max-heap (small). Since Python's heapq is min-heap,
        # we push the negative value.
        heapq.heappush(self.small, -num)
        
        # Balance heaps to ensure that small's root is always less than large's root
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # If sizes are unbalanced, balance them by moving an element from the larger heap to the smaller one
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If the number of elements is odd, the median is the root of the larger heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If the number of elements is even, the median is the average of the roots of both heaps
        else:
            return (-self.small[0] + self.large[0]) / 2.0