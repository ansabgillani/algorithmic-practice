class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_scores = {}
        
        # Count the score of each prefix
        for word in words:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                prefix_scores[prefix] = prefix_scores.get(prefix, 0) + 1
        
        # Calculate the sum of scores for each word
        result = []
        for word in words:
            total_score = sum(prefix_scores[prefix] for prefix in (word[:i] for i in range(1, len(word) + 1)))
            result.append(total_score)
        
        return result