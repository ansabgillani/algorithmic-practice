class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Apply operations to the array
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift all zeroes to the end of the array
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        
        return nums

# Example usage:
sol = Solution()
print(sol.applyOperations([1,2,2,1,1,0]))  # Output: [1,4,2,0,0,0]
print(sol.applyOperations([0,1]))          # Output: [1,0]