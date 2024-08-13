class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, remaining):
            if remaining == 0:
                self.result.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if remaining - candidates[i] < 0:
                    break
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])
        
        self.result = []
        candidates.sort()
        backtrack(0, [], target)
        return self.result