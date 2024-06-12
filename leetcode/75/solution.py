class Solution:
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        current = 0
        
        while current <= high:
            if nums[current] == 0:
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 2:
                nums[high], nums[current] = nums[current], nums[high]
                high -= 1
            else:
                current += 1

# Example usage
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)  # Output: [0,0,1,1,2,2]

nums = [2,0,1]
Solution().sortColors(nums)
print(nums)  # Output: [0,1,2]