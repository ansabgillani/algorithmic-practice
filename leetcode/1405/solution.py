import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap with negative counts to simulate max-heap using Python's min-heap
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)
            
            # Add the two most frequent characters to the result
            if -count1 > 2:
                result.extend([char1] * 2)
                count1 += 4  # Increase by 4 because we added 2 characters
            else:
                result.extend([char1] * (-count1))
                count1 = 0
            
            if -count2 > 2:
                result.extend([char2] * 2)
                count2 += 4  # Increase by 4 because we added 2 characters
            else:
                result.extend([char2] * (-count2))
                count2 = 0
                
            if count1 < 0:
                heapq.heappush(max_heap, (count1, char1))
            if count2 < 0:
                heapq.heappush(max_heap, (count2, char2))
        
        # Handle the remaining character if any
        if max_heap:
            count, char = max_heap[0]
            result.extend([char] * min(2, -count))
        
        return ''.join(result)