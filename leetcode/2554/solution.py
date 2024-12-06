class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Convert banned to set for O(1) lookups
        banned_set = set(banned)
        
        # Initialize sum and count of chosen numbers
        current_sum = 0
        count = 0
        
        # Iterate through the range [1, n]
        for i in range(1, n + 1):
            # If i is not banned and adding it does not exceed maxSum
            if i not in banned_set and current_sum + i <= maxSum:
                count += 1
                current_sum += i
        
        return count