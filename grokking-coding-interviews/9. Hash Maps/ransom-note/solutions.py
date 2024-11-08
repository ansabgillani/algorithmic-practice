from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in both strings
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        # Check if ransomNote can be constructed from magazine
        for char, count in ransomCount.items():
            if magazineCount[char] < count:
                return False
        return True

# Test cases to verify the solution
print(Solution().canConstruct("a", "b"))  # Output: False
print(Solution().canConstruct("aa", "ab"))  # Output: False
print(Solution().canConstruct("aa", "aab"))  # Output: True