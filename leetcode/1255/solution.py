class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_scores = {chr(i + 97): score[i] for i in range(26)}
        letter_counts = Counter(letters)

        def get_word_score(word):
            return sum(letter_scores[letter] * word.count(letter) for letter in set(word))

        max_score = 0

        def backtrack(start, current_score, remaining_letters):
            nonlocal max_score
            max_score = max(max_score, current_score)
            for i in range(start, len(words)):
                word = words[i]
                word_counts = Counter(word)
                if all(remaining_letters[letter] >= word_counts[letter] for letter in word):
                    remaining_letters -= word_counts
                    backtrack(i + 1, current_score + get_word_score(word), remaining_letters)
                    remaining_letters += word_counts

        backtrack(0, 0, letter_counts)
        
        return max_score