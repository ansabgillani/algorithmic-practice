class Solution:
    def minChanges(self, s: str) -> int:
        # Initialize the count of changes required
        changes = 0
        
        # Iterate through the string in steps of 2
        for i in range(0, len(s), 2):
            # Check if the current and next character are not the same
            if s[i] != s[i + 1]:
                # Increment the change count
                changes += 1
        
        return changes

# Example usage:
# sol = Solution()
# print(sol.minChanges("1001"))  # Output: 2
# print(sol.minChanges("10"))    # Output: 1
# print(sol.minChanges("0000"))  # Output: 0