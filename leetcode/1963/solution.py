class Solution:
    def minSwaps(self, s: str) -> int:
        open_brackets = 0
        close_brackets = 0
        swaps = 0
        imbalance = 0
        
        for char in s:
            if char == '[':
                open_brackets += 1
                if imbalance > 0:
                    swaps += imbalance // 2
                    imbalance -= imbalance // 2
            else:
                close_brackets += 1
                imbalance = close_brackets - open_brackets
        
        return swaps

# Example usage:
# sol = Solution()
# print(sol.minSwaps("][]["))  # Output: 1
# print(sol.minSwaps("]]][[[ "))  # Output: 2
# print(sol.minSwaps("[]"))  # Output: 0