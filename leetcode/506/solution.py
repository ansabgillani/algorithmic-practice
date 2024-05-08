class Solution:
    def findRelativeRanks(self, score):
        rank_map = {s: '' for s in score}
        sorted_scores = sorted(score, reverse=True)
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = 'Gold Medal'
            elif i == 1:
                rank_map[s] = 'Silver Medal'
            elif i == 2:
                rank_map[s] = 'Bronze Medal'
            else:
                rank_map[s] = str(i + 1)
        return [rank_map[s] for s in score]