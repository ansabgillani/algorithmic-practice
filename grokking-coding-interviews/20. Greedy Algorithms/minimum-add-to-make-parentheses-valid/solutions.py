class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        extra_closing = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    extra_closing += 1
                    
        return balance + extra_closing