class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        effective_time = time % (2 * (n - 1))
        if effective_time < n:
            return effective_time + 1
        else:
            return 2 * (n - 1) - effective_time + 1