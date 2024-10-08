class Solution:
    def min_swaps_to_balance(self, s):
        n = len(s)
        left_balance, right_balance = 0, 0
        max_swaps, current_swaps = 0, 0

        # Traverse from left to right
        for char in s:
            if char == '[':
                left_balance += 1
            else:
                left_balance -= 1
        
            # Adjust current swaps needed for balance
            if left_balance < 0:
                current_swaps = max(current_swaps, -left_balance)
                left_balance = 0

        # Reset and traverse from right to left
        left_balance, right_balance = 0, 0
        for char in reversed(s):
            if char == ']':
                right_balance += 1
            else:
                right_balance -= 1
        
            # Adjust current swaps needed for balance
            if right_balance < 0:
                max_swaps = max(max_swaps, -right_balance)
                right_balance = 0

        return (max_swaps + current_swaps) // 2