class Solution:
    def countSubarrays(self, nums, minK, maxK):
        def helper(minK, maxK):
            res = left = 0
            minL = maxL = -1
            
            for right, n in enumerate(nums):
                if n == minK: 
                    minL = right
                if n == maxK:
                    maxL = right
                if not (minL >= 0 and maxL >= 0): 
                    continue
                left = min(minL, maxL)
                res += left - left + 1
            
            return res
        
        return helper(minK, maxK) - helper(minK+1, maxK+1)