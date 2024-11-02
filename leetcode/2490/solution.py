class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Check if first and last character match
        if sentence[0] != sentence[-1]:
            return False
        
        # Split words and check each word's last character matches next word's first character
        words = sentence.split()
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        
        return True