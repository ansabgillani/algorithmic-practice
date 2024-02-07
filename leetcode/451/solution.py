from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Use a max heap to sort characters by frequency
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)
        
        # Build the result string
        result = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char * -freq)
        
        return ''.join(result)

# Example usage:
# sol = Solution()
# print(sol.frequencySort("tree"))  # Output: "eert"
# print(sol.frequencySort("cccaaa"))  # Output: "aaaccc"
# print(sol.frequencySort("Aabb"))  # Output: "bbAa"