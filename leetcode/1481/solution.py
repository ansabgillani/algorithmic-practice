from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each integer in the array
        freq = Counter(arr)
        
        # Sort the frequencies in ascending order
        sorted_freq = sorted(freq.values())
        
        # Remove elements starting from the least frequent ones
        for i, f in enumerate(sorted_freq):
            if k >= f:
                k -= f
            else:
                break
        
        # The number of unique integers left is the length minus the number of removed items
        return len(freq) - (i + 1)