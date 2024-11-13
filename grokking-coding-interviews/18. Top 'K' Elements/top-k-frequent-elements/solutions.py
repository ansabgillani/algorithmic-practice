from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements from the array nums.
        
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count the frequency of each element
        count = Counter(nums)
        
        # Use a min heap to keep track of top k frequent elements
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        
        # Extract the elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        return result[::-1]