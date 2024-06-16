class Solution:
    def minPatches(self, nums, n):
        maxReach = 0
        i = 0
        patches = 0
        
        while maxReach < n:
            if i < len(nums) and nums[i] <= maxReach + 1:
                maxReach += nums[i]
                i += 1
            else:
                maxReach += (maxReach + 1)
                patches += 1
    
        return patches