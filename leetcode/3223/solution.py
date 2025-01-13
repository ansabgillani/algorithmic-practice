class Solution:
    def minLength(self, s: str) -> int:
        # Initialize a stack to keep track of characters that can be paired and removed
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if stack and stack[-1] == char:
                # If the current character matches the top of the stack, pop it (they form a pair)
                stack.pop()
            else:
                # Otherwise, push the current character onto the stack
                stack.append(char)
        
        # The length of the remaining string is the number of characters in the stack
        return len(stack)

# Example usage:
solution = Solution()
print(solution.minLength("abaacbcbb"))  # Output: 5
print(solution.minLength("aa"))         # Output: 2