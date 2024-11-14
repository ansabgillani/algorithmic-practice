class Solution:
    def minimizedMaximum(self, n, quantities):
        # Helper function to check if given max products is feasible
        def isFeasible(max_prod):
            total_stores = 0
            for q in quantities:
                total_stores += (q + max_prod - 1) // max_prod  # Ceiling division
            return total_stores <= n

        # Binary search for the minimum possible maximum products
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
    
        return left

# Example usage
print(Solution().minimizedMaximum(6, [11, 6]))  # Output: 3
print(Solution().minimizedMaximum(7, [15, 10, 10]))  # Output: 5
print(Solution().minimizedMaximum(1, [100000]))  # Output: 100000