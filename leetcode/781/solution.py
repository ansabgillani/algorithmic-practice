from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the frequency of each answer
        count = Counter(answers)
        
        total_rabbits = 0
        for answer, freq in count.items():
            # Calculate the number of groups needed for this answer
            groups = (freq + answer) // (answer + 1)
            # Each group has (answer + 1) rabbits
            total_rabbits += groups * (answer + 1)
        
        return total_rabbits