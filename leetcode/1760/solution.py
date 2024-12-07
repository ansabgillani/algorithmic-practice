class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to check if we can achieve the desired penalty
        def canAchieve(penalty):
            operations = 0
            for num in nums:
                if num > penalty:
                    operations += (num - 1) // penalty
                    if operations > maxOperations:
                        return False
            return True
        
        # Binary search on the possible penalty values
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchieve(mid):
                right = mid
            else:
                left = mid + 1
                
        return left

# Example usage:
# sol = Solution()
# print(sol.minimumSize([9], 2))  # Output: 3
# print(sol.minimumSize([2,4,8,2], 4))  # Output: 2