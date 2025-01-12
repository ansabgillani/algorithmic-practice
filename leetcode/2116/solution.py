class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        balance = 0
        open_count = 0
        
        for i in range(len(s)):
            if locked[i] == '1':
                balance += 1 if s[i] == '(' else -1
                if balance < 0:
                    return False
            else:
                open_count += 1
            
        # Check if we have enough open positions to match closing parentheses.
        if (balance + open_count) % 2 != 0:
            return False
        
        reverse_balance = 0
        close_count = 0
        
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '1':
                reverse_balance += 1 if s[i] == ')' else -1
                if reverse_balance < 0:
                    return False
            else:
                close_count += 1
        
        # Check if we have enough close positions to match opening parentheses.
        if (reverse_balance + close_count) % 2 != 0:
            return False
        
        return True