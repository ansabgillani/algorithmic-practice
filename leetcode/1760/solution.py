class Solution:
    def minimumSize(self, nums, maxOperations):
        low, high = 1, max(nums)
        
        while low < high:
            mid = (low + high) // 2
            ops = sum((x - 1) // mid for x in nums)
            
            if ops <= maxOperations:
                high = mid
            else:
                low = mid + 1
                
        return low