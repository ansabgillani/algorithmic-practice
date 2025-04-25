from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Transform the array to a prefix of counts where each element is 1 if nums[i] % modulo == k else 0
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + (num % modulo == k))
        
        count = defaultdict(int)
        result = 0
        
        # Iterate over the prefix array to find valid subarrays
        for i, p in enumerate(prefix):
            target = (p - k) % modulo
            if target in count:
                result += count[target]
            count[p % modulo] += 1
        
        return result

# Example usage:
# sol = Solution()
# print(sol.countInterestingSubarrays([3,2,4], 2, 1))  # Output: 3
# print(sol.countInterestingSubarrays([3,1,9,6], 3, 0))  # Output: 2