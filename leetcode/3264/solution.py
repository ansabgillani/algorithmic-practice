class Solution:
    def finalArray(self, nums, k, multiplier):
        heap = []
        for num in nums:
            self.heappush(heap, num)
        
        for _ in range(k):
            min_val = self.heappop(heap)
            new_val = min_val * multiplier
            self.heappush(heap, new_val)
        
        return list(heap)
    
    def heappush(self, heap, item):
        if not heap:
            heap.append(item)
        else:
            heap.append(item)
            i = len(heap) - 1
            while i > 0 and heap[(i-1)//2] > heap[i]:
                heap[(i-1)//2], heap[i] = heap[i], heap[(i-1)//2]
                i = (i-1)//2
    
    def heappop(self, heap):
        if not heap:
            return None
        min_val = heap[0]
        last_item = heap.pop()
        if heap:
            self.heapify(heap, 0)
        return min_val
    
    def heapify(self, heap, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(heap, smallest)