class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initialize counters
        count_a = 0
        deletions = 0
        
        # Iterate through the string
        for char in s:
            if char == 'a':
                count_a += 1
            else:
                # If we encounter a 'b' before any 'a', it needs to be deleted
                if count_a > 0:
                    deletions += 1
        
        return deletions

# Example usage:
sol = Solution()
print(sol.minimumDeletions("aababbab"))  # Output: 2
print(sol.minimumDeletions("bbaaaaabb"))  # Output: 2