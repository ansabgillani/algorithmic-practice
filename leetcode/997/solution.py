from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Finds the town judge if exists.
        
        :param n: Number of people in the town.
        :param trust: A list of trust relationships where each relationship is a pair [a_i, b_i].
        :return: The label of the town judge or -1 if no such person exists.
        """
        # Edge case: If there's only one person and no trusts, they are the judge
        if n == 1 and not trust:
            return 1
        
        # Initialize in-degree and out-degree arrays
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        # Update degrees based on trust relationships
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        
        # Find the person with exactly n-1 in-degrees and 0 out-degrees
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        
        return -1