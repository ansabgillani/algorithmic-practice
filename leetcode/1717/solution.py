class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Function to remove all occurrences of 'a' followed by 'b'
        def removeAllAB(s: str, score: int, a: str, b: str) -> tuple:
            while a + b in s:
                s = s.replace(a + b, '', 1)
                score += 1
            return s, score

        # Determine which substring to process first based on their scores
        if x > y: 
            s, score = removeAllAB(s, 0, 'a', 'b')
            s, score = removeAllAB(s, score, 'b', 'a')
        else:
            s, score = removeAllAB(s, 0, 'b', 'a')
            s, score = removeAllAB(s, score, 'a', 'b')

        return score