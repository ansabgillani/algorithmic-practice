class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        P = [0]*(n+1)
        L = [0]*(n+1)
        A = [0]*(n+1)

        P[0] = 1
        A[0] = 1

        for i in range(1, n+1):
            P[i] = (P[i-1] + L[i-1] + A[i-1]) % mod
            L[i] = (P[i-1] + L[i-1]) % mod
            A[i] = sum(P[:i]) % mod

        return (P[n] + L[n] + A[n]) % mod