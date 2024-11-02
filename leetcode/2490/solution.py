class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Check if the first character of each word matches the last character of the previous word
        for i in range(len(words)):
            if i == 0 and words[i][-1] != words[-1][0]:
                return False
            elif words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        
        return True

# Example usage:
sol = Solution()
print(sol.isCircularSentence("leetcode exercises sound delightful"))  # Output: True
print(sol.isCircularSentence("eetcode"))                               # Output: True
print(sol.isCircularSentence("Leetcode is cool"))                    # Output: False