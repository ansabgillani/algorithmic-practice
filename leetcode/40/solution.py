class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in 'candidates' where the candidate numbers sum to 'target'.
        Each number in 'candidates' may only be used once in the combination.
        
        :param candidates: List of candidate numbers
        :param target: Target sum for the combination
        :return: List of unique combinations that sum up to the target
        """
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
        
        result = []
        candidates.sort()  # Sort the candidates to handle duplicates easily
        backtrack(0, [], target)
        return result