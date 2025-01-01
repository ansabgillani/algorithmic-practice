class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Helper function to count the number of subarrays with sum <= target
        def count_subarrays(target):
            count = 0
            current_sum = 0
            j = 0
            for i in range(n):
                while j < n and current_sum + nums[j] <= target:
                    current_sum += nums[j]
                    j += 1
                count += j - i
                if j > 0:
                    current_sum -= nums[i]
            return count
        
        left, right = min(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if count_subarrays(mid) >= k:
                right = mid
            else:
                left = mid + 1
                
        return left