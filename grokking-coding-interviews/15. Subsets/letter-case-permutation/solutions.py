class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Generate all possible strings by transforming each letter in the input string 's' 
        to either lowercase or uppercase.
        
        :param s: Input string
        :return: List of all possible transformed strings
        """
        result = []
        
        def backtrack(index):
            if index == len(s):
                result.append(''.join(path))
                return
            
            current_char = s[index]
            
            # Option 1: Keep the character as is
            path.append(current_char)
            backtrack(index + 1)
            path.pop()
            
            # Option 2: Convert to opposite case
            if current_char.isalpha():
                if current_char.islower():
                    path.append(current_char.upper())
                else:
                    path.append(current_char.lower())
                backtrack(index + 1)
                path.pop()
        
        path = []
        backtrack(0)
        return result

# Test cases
sol = Solution()
print(sol.letterCasePermutation("a1b2"))  # Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
print(sol.letterCasePermutation("3z4"))   # Output: ["3z4", "3Z4"]