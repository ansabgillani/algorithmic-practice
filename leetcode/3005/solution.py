class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Dictionary to store frequency of each element
        freq = {}
        
        # Count the frequency of each element
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Calculate the total frequencies of elements with maximum frequency
        total_max_freq_elements = sum(count for count in freq.values() if count == max_freq)
        
        return total_max_freq_elements