class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        
        # Count frequency of each character
        count = Counter(s)
        max_heap = []
        
        # Push all characters into max heap with negative frequency for max-heap behavior
        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))
        
        result = []
        prev_char = None
        prev_freq = 0
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            
            if prev_char is not None and prev_freq != 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
                prev_char = None
                prev_freq = 0
            
            # Append the character up to repeatLimit times
            for _ in range(min(-freq, repeatLimit)):
                result.append(char)
            
            # Update previous character and frequency
            if freq < -repeatLimit:
                prev_char = char
                prev_freq = freq + repeatLimit
        
        return ''.join(result)