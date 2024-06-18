from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulties and profits into pairs and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Initialize variables to track the maximum profit so far and total earnings
        max_profit_so_far = 0
        total_earnings = 0
        
        # Process each job in sorted order
        for i in range(len(jobs)):
            difficulty_i, profit_i = jobs[i]
            max_profit_so_far = max(max_profit_so_far, profit_i)
            
            # Update the maximum profit for all workers who can do this job
            while worker and worker[-1] >= difficulty_i:
                total_earnings += max_profit_so_far
                worker.pop()
        
        return total_earnings