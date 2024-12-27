class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Finds the maximum score of a pair of sightseeing spots.
        
        :type values: List[int]
        :rtype: int
        """
        max_score = 0
        max_i_plus_values = values[0] + 0
        
        for j in range(1, len(values)):
            max_score = max(max_score, max_i_plus_values + values[j] - j)
            max_i_plus_values = max(max_i_plus_values, values[j] + j)
        
        return max_score