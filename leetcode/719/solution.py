from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th smallest distance among all pairs of numbers in the given array.
        
        Args:
            nums: List[int] - The input list of integers.
            k: int - The order of the smallest distance to find.
            
        Returns:
            int - The k-th smallest distance.
        """
        def count_pairs(distance):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > distance:
                    left += 1
                count += (right - left)
            return count
        
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low

# Example usage:
sol = Solution()
print(sol.smallestDistancePair([1,3,1], 1))  # Output: 0
print(sol.smallestDistancePair([1,1,1], 2))  # Output: 0
print(sol.smallestDistancePair([1,6,1], 3))  # Output: 5