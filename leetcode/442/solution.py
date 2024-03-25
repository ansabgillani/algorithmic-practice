class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            
            if nums[index] < 0:
                duplicates.append(abs(index) + 1)
            else:
                nums[index] = -nums[index]
        
        return duplicates