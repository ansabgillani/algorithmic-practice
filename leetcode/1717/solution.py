class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Helper function to remove all occurrences of a substring from a string
        def remove_substring(s, sub):
            stack = []
            for char in s:
                if not stack or stack[-1] != sub[0]:
                    stack.append(char)
                elif stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)
        
        # Determine the order of removal based on the points
        if x >= y:
            first_sub = 'ab'
            second_sub = 'ba'
            first_points = x
            second_points = y
        else:
            first_sub = 'ba'
            second_sub = 'ab'
            first_points = y
            second_points = x
        
        # Remove the higher point substring as many times as possible
        s = remove_substring(s, first_sub)
        points = s.count(first_sub) * first_points
        
        # Remove the remaining substring
        s = remove_substring(s, second_sub)
        points += s.count(second_sub) * second_points
        
        return points

# Example usage:
# solution = Solution()
# print(solution.maximumGain("cdbcbbaaabab", 4, 5))  # Output: 19
# print(solution.maximumGain("aabbaaxybbaabb", 5, 4))  # Output: 20