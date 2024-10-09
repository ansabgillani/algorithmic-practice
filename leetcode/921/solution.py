class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters for open and close parentheses
        open_count = 0
        close_count = 0
        
        # Iterate through each character in the string
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
        
        # The total moves required is the sum of unmatched open and close parentheses
        return open_count + close_count

# Example usage:
# solution = Solution()
# print(solution.minAddToMakeValid("())"))  # Output: 1
# print(solution.minAddToMakeValid("((("))  # Output: 3