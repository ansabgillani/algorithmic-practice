class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge case: if k is less than or equal to 1, no subarray can have a product less than k
        if k <= 1:
            return 0

        left = 0
        prod = 1
        result = 0

        for right in range(len(nums)):
            # Multiply the current element with the product of the existing window
            prod *= nums[right]
            
            # If the product is greater than or equal to k, shrink the window from the left
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1
            
            # The number of valid subarrays ending at 'right' is (right - left + 1)
            result += right - left + 1

        return result