class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Initialize pointers and counters
        left = 0
        right = 0
        last_minK_index = -1
        last_maxK_index = -1
        result = 0
        
        while right < len(nums):
            if nums[right] < minK or nums[right] > maxK:
                # Reset pointers and counters
                left = right + 1
                last_minK_index = -1
                last_maxK_index = -1
            else:
                # Update the indices of minK and maxK
                if nums[right] == minK:
                    last_minK_index = right
                if nums[right] == maxK:
                    last_maxK_index = right
                
                # Calculate the number of valid subarrays ending at right
                result += max(0, min(last_minK_index, last_maxK_index) - left + 1)
            
            right += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.countSubarrays([1,3,5,2,7,5], 1, 5))  # Output: 2
print(solution.countSubarrays([1,1,1,1], 1, 1))      # Output: 10