class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate total number of happy strings of length n
        total = 3 * (2 ** (n - 1))
        
        if k > total:
            return ""
        
        result = []
        
        # Convert k to a base-3 representation with '0' and '1'
        for i in range(n):
            digit = (k - 1) % 2
            k //= 2
            
            if digit == 0:
                last_char = result[-1] if result else ''
                if last_char != 'a':
                    result.append('a')
                elif last_char != 'b':
                    result.append('b')
                else:
                    result.append('c')
            else:
                last_char = result[-1] if result else ''
                if last_char != 'c':
                    result.append('c')
                elif last_char != 'b':
                    result.append('b')
                else:
                    result.append('a')
        
        return ''.join(result)