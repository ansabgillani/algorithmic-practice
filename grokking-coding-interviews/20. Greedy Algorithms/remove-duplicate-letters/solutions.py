class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Dictionary to store last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        # Stack to store the result characters
        stack = []
        # Set to check if a character is already in the stack
        seen = set()
        
        for i, char in enumerate(s):
            # Skip if the character is already in the stack
            if char in seen:
                continue
            
            # While stack is not empty and current char is smaller than last char
            # in stack and last occurrence of that char is after current index,
            # pop from stack and mark the popped element as unseen
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            
            # Add current character to stack and mark it as seen
            stack.append(char)
            seen.add(char)
        
        # Join characters in stack to form the final result
        return ''.join(stack)

# Test cases:
solution = Solution()
print(solution.removeDuplicateLetters("bcabc"))  # Output: "abc"
print(solution.removeDuplicateLetters("cbacdcbc"))  # Output: "acdb"