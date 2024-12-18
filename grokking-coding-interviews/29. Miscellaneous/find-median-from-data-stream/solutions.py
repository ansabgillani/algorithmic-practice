import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap for smaller half of numbers
        self.large = []  # Min-heap for larger half of numbers
        
    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0]