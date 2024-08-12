class Solution:
    def __init__(self, k: int, nums):
        self.heap = nums[:k]
        self.k = k
        for num in nums[k:]:
            if num > self.heap[0]:
                self.heapreplace(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heappush(val)
        elif val > self.heap[0]:
            self.heapreplace(val)
        
        return self.heap[0]

    def heappush(self, val):
        if len(self.heap) < self.k:
            self.heap.append(val)
            i = len(self.heap) - 1
            while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
                self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                i = (i-1)//2

    def heapreplace(self, val):
        self.heap[0] = val
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break