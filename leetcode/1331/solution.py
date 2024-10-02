class Solution:
    def array_rank_transform(self, arr):
        sorted_unique = sorted(set(arr))
        rank_map = {value: idx + 1 for idx, value in enumerate(sorted_unique)}
        return [rank_map[value] for value in arr]