class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a number satisfies the partition condition
        def can_partition(num, target):
            num_str = str(num)
            length = len(num_str)
            
            @lru_cache(None)
            def dp(index, current_sum):
                if index == length:
                    return current_sum == target
                
                total = 0
                for i in range(index, length):
                    total = total * 10 + int(num_str[i])
                    if dp(i + 1, current_sum + total):
                        return True
                return False
            
            return dp(0, 0)
        
        # Calculate the punishment number by summing squares of all valid numbers
        return sum(i**2 for i in range(1, n+1) if can_partition(i*i, i))

# Example usage:
solution = Solution()
print(solution.punishmentNumber(10))  # Output: 182
print(solution.punishmentNumber(37))  # Output: 1478