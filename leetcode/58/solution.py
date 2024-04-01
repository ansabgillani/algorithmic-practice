class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces and split the string into words
        words = s.rstrip().split()
        
        # Return the length of the last word
        return len(words[-1])