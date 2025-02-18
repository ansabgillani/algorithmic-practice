class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Construct the lexicographically smallest number from a given DI string.
        
        :param pattern: A string consisting of 'I' and 'D' characters.
        :return: The lexicographically smallest possible string that meets the conditions.
        """
        n = len(pattern)
        stack = []
        num = 1
        
        for char in pattern:
            if char == 'I':
                stack.append(num)
                while stack:
                    num += 1
                    yield str(stack.pop())
            else:
                stack.append(num)
                num += 1
        
        # Push the last number
        stack.append(num)
        while stack:
            yield str(stack.pop())

# Example usage:
sol = Solution()
print(sol.smallestNumber("IIIDIDDD"))  # Output: "123549876"
print(sol.smallestNumber("DDD"))       # Output: "4321"