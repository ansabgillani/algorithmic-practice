from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of each element in the current window
        freq = defaultdict(int)
        
        # Variables to track the number of valid subarrays and the start index of the window
        count = 0
        start = 0
        pairs = 0
        
        # Iterate over the array with the end pointer
        for end in range(len(nums)):
            # Update frequency of the current element
            freq[nums[end]] += 1
            
            # If there are more than one occurrence of nums[end], it contributes to the number of pairs
            if freq[nums[end]] > 1:
                pairs += (freq[nums[end]] - 1)
            
            # While we have at least k pairs, count all subarrays ending at 'end' and starting from any index >= start
            while pairs >= k:
                count += (len(nums) - end)
                freq[nums[start]] -= 1
                if freq[nums[start]] > 0:
                    pairs -= (freq[nums[start]])
                start += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.countGood([1,1,1,1,1], 10))  # Output: 1
# print(sol.countGood([3,1,4,3,2,2,4], 2))  # Output: 4