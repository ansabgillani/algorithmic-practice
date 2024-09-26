class Solution:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        index = self.bisect(self.events, [start, end])
        
        if (index == 0 or self.events[index - 1][1] <= start) and \
           (index == len(self.events) or end <= self.events[index][0]):
            self.events.insert(index, [start, end])
            return True

        return False

    def bisect(self, arr, x):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] >= x[0]:
                right = mid
            else:
                left = mid + 1
        return left