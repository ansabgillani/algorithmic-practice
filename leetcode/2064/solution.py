class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if it's possible to distribute products such that no store gets more than 'max_products'
        def can_distribute(max_products):
            total_stores = 0
            for quantity in quantities:
                total_stores += (quantity + max_products - 1) // max_products
            return total_stores <= n
        
        # Binary search to find the minimum possible maximum number of products per store
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Example usage:
solution = Solution()
print(solution.minimizedMaximum(6, [11, 6]))  # Output: 3
print(solution.minimizedMaximum(7, [15, 10, 10]))  # Output: 5
print(solution.minimizedMaximum(1, [100000]))  # Output: 100000