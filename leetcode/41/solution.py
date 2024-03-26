class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Replace negative numbers and numbers larger than n with 0
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        
        # Step 2: Use index as a hash key and number sign as a presence detector
        for num in nums:
            idx = abs(num) - 1
            if idx < n:
                nums[idx] = -abs(nums[idx])
        
        # Step 3: The first positive index + 1 indicates the missing smallest positive integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1

# Test cases to verify the solution
print(Solution().firstMissingPositive([1,2,0]))  # Output: 3
print(Solution().firstMissingPositive([3,4,-1,1]))  # Output: 2
print(Solution().firstMissingPositive([7,8,9,11,12]))  # Output: 1