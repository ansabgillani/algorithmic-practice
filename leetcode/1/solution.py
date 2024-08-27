class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            else:
                num_dict[num] = i

# Example usage:
sol = Solution()
nums1, target1 = [2, 7, 11, 15], 9
print(sol.twoSum(nums1, target1))  # Output: [0, 1]

nums2, target2 = [3, 2, 4], 6
print(sol.twoSum(nums2, target2))  # Output: [1, 2]

nums3, target3 = [3, 3], 6
print(sol.twoSum(nums3, target3))  # Output: [0, 1]