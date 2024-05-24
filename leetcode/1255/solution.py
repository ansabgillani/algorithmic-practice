class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        
        # Count the frequency of each letter in letters
        letter_count = Counter(letters)
        
        # Helper function to calculate the score of a word given the letter count
        def calculate_score(word, letter_count):
            return sum(score[ord(char) - ord('a')] * word.count(char) for char in set(word))
        
        # Recursive helper function to find the maximum score
        def dfs(index=0, current_score=0, current_letter_count=letter_count):
            if index == len(words):
                return current_score
            
            max_score = 0
            # Option to include the current word
            if all(current_letter_count[char] >= words[index].count(char) for char in set(words[index])):
                new_letter_count = Counter(current_letter_count)
                for char in set(words[index]):
                    new_letter_count[char] -= words[index].count(char)
                max_score = max(max_score, dfs(index + 1, current_score + calculate_score(words[index], new_letter_count), new_letter_count))
            
            # Option to exclude the current word
            max_score = max(max_score, dfs(index + 1, current_score, current_letter_count))
            
            return max_score
        
        return dfs()