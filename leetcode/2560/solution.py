class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Helper function to check if a given capability can be achieved by robbing at least k houses
        def can_rob_with_capability(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2  # Skip the next house as we cannot rob adjacent houses
                else:
                    i += 1
            return count >= k
        
        # Binary search to find the minimum capability
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid
            else:
                left = mid + 1
        
        return left