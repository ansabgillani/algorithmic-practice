class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        max_freq = max(freq.values())
        total = sum(val for val in freq.values() if val == max_freq)
        
        return total

# Example usage:
solution = Solution()
print(solution.maxFrequencyElements([1,2,2,3,1,4]))  # Output: 4
print(solution.maxFrequencyElements([1,2,3,4,5]))    # Output: 5