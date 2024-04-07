class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Check if the given string of parentheses and asterisks is valid.
        
        :type s: str
        :rtype: bool
        """
        leftBalance = rightBalance = 0
        
        for char in s:
            # Increment balances based on character
            leftBalance += 1 if char == '(' or char == '*' else -1
            rightBalance += 1 if char == ')' or char == '*' else -1
            
            # If balance goes negative, return False as it's invalid
            if leftBalance < 0 or rightBalance < 0:
                return False
        
        # Final balances must be non-negative to be valid
        return leftBalance >= 0 and rightBalance >= 0

# Test cases
assert Solution().checkValidString("()") == True
assert Solution().checkValidString("(*)") == True
assert Solution().checkValidString("(*))") == True