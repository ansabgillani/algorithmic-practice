class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        total_profit, max_profit_so_far = 0, 0
        
        for diff, prof in jobs:
            max_profit_so_far = max(max_profit_so_far, prof)
        
        for w in worker:
            if w >= jobs[-1][0]:
                total_profit += max_profit_so_far
            elif w < jobs[0][0]:
                break
            else:
                i = 0
                while i < len(jobs) and jobs[i][0] <= w:
                    i += 1
                total_profit += jobs[i-1][1]
        
        return total_profit