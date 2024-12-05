class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Check if counts of 'L', 'R' and '_' are the same in both strings
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        i = j = 0
        n = len(start)
        
        while i < n or j < n:
            # Move pointers to the next non-blank character
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            # If both pointers are at the end, strings are valid
            if i == n and j == n:
                return True
            
            # If one pointer is at the end but not both, strings are invalid
            if i == n or j == n:
                return False
            
            # Check if pieces are different or 'L' cannot move right or 'R' cannot move left
            if (start[i] != target[j]) or (start[i] == 'L' and i < j) or (target[j] == 'R' and i > j):
                return False
            
            i += 1
            j += 1
        
        return True

# Example usage:
sol = Solution()
print(sol.canChange("_L__R__R_", "L______RR"))  # Output: true
print(sol.canChange("R_L_", "__LR"))           # Output: false
print(sol.canChange("_R", "R_"))               # Output: false