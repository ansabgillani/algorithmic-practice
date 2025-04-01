class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        # Create a DP array to store the maximum points from index i onwards
        dp = [0] * (n + 1)
        
        # Iterate backwards through the questions
        for i in range(n - 1, -1, -1):
            # Option 1: Skip the current question
            skip_current = dp[i + 1]
            
            # Option 2: Solve the current question
            solve_current = questions[i][0]
            if i + questions[i][1] + 1 < n:
                solve_current += dp[i + questions[i][1] + 1]
            
            # Store the maximum points from both options
            dp[i] = max(skip_current, solve_current)
        
        # The answer is the maximum points starting from index 0
        return dp[0]