from collections import Counter

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Count the frequency of each number in nums
        num_counts = Counter(nums)
        
        # Sort the keys by their absolute values
        sorted_nums = sorted(num_counts.keys(), key=abs)
        
        distinct_count = 0
        
        for num in sorted_nums:
            if num_counts[num] > 1:
                # If we can reduce the count of this number to 1, do it
                if k >= abs(num_counts[num]) - 1:
                    k -= (abs(num_counts[num]) - 1)
                    distinct_count += 1
                    num_counts[num] = 1
            else:
                # If the count is already 1, we keep this number distinct
                distinct_count += 1
        
        # Add any remaining numbers that can be made distinct by adjusting k
        distinct_count += min(k, len(sorted_nums) - distinct_count)
        
        return distinct_count

# Test cases
print(Solution().maxDistinctElements([1,2,3,4], k=1))  # Output: 4
print(Solution().maxDistinctElements([1,2,2,3,4], k=1))  # Output: 4
print(Solution().maxDistinctElements([1,1,1,1], k=1))  # Output: 1