class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the remainder and its corresponding index
        remainder_map = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            if k != 0:
                current_sum %= k
            
            if current_sum in remainder_map:
                # Check if the subarray length is at least two
                if i - remainder_map[current_sum] > 1:
                    return True
            else:
                # Store the first occurrence of this remainder
                remainder_map[current_sum] = i
        
        return False

# Test cases to verify the solution
assert Solution().checkSubarraySum([23,2,4,6,7], 6) == True
assert Solution().checkSubarraySum([23,2,6,4,7], 6) == True
assert Solution().checkSubarraySum([23,2,6,4,7], 13) == False