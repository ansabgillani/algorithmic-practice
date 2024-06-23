class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Initialize two deques to store indices of minimum and maximum values
        min_deque = []
        max_deque = []
        left = 0
        result = 0
        
        for right in range(len(nums)):
            # Maintain the deque of indices with increasing values
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain the deque of indices with decreasing values
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Ensure the difference between the maximum and minimum values is within the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if min_deque[0] < left:
                    min_deque.pop(0)
                if max_deque[0] < left:
                    max_deque.pop(0)
            
            # Update the result with the maximum subarray length found so far
            result = max(result, right - left + 1)
        
        return result

# Example usage:
solution = Solution()
print(solution.longestSubarray([8,2,4,7], 4))  # Output: 2
print(solution.longestSubarray([10,1,2,4,7,2], 5))  # Output: 4
print(solution.longestSubarray([4,2,2,2,4,4,2,2], 0))  # Output: 3