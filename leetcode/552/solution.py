class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize DP arrays
        dp_A = [0] * (n+1)
        dp_L = [0] * (n+1)
        dp_PL = [0] * (n+1)
        
        dp_A[0] = dp_L[0] = dp_PL[0] = 1
        
        for i in range(1, n+1):
            dp_A[i] = (dp_A[i-1] + dp_L[i-1] + dp_PL[i-1]) % MOD
            dp_L[i] = dp_PL[i-1]
            dp_PL[i] = dp_L[i-1]
        
        return (dp_A[n] + dp_L[n] + dp_PL[n]) % MOD