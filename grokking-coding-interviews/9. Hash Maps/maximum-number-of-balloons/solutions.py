from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the frequency of each character in the text
        char_count = Counter(text)
        
        # Define the required characters and their minimum counts to form "balloon"
        required_chars = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        # Calculate the maximum number of balloons that can be formed
        min_count = float('inf')
        for char, count in required_chars.items():
            if char not in char_count:
                return 0
            min_count = min(min_count, char_count[char] // count)
        
        return min_count

# Test cases to verify the solution
solution = Solution()
print(solution.maxNumberOfBalloons("nlaebolko"))  # Output: 1
print(solution.maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2
print(solution.maxNumberOfBalloons("leetcode"))  # Output: 0