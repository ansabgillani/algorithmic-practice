class Solution:
    def maxScore(self, s: str) -> int:
        """
        Finds the maximum score after splitting the string into two non-empty substrings.
        
        The score is calculated as the number of '0's in the left substring plus the number 
        of '1's in the right substring.
        
        Args:
        s (str): Input string consisting of '0's and '1's.
        
        Returns:
        int: Maximum score achievable by splitting the string.
        """
        # Count total number of '1's in the string
        total_ones = s.count('1')
        max_score = 0
        current_zeros = 0
        
        # Iterate through the string except the last character
        for char in s[:-1]:
            if char == '0':
                current_zeros += 1
            else:
                total_ones -= 1
            
            # Calculate score for the current split
            score = current_zeros + total_ones
            max_score = max(max_score, score)
        
        return max_score

# Test cases
solution = Solution()
print(solution.maxScore("011101"))  # Output: 5
print(solution.maxScore("00111"))   # Output: 5
print(solution.maxScore("1111"))    # Output: 3