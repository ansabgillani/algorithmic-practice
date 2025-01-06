class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])
        
        result = []
        backtrack(0, target, [])
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(solution.combinationSum([2, 3, 5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(solution.combinationSum([2], 1))           # Output: []