class Solution:
    def minIncrementForUnique(self, A):
        if not A:
            return 0
        A.sort() 
        res = 0 
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += (A[i-1] - A[i]) + 1
                A[i] = A[i-1] + 1
        return res