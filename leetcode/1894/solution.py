class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        for i, c in enumerate(chalk):
            k -= c
            if k < 0:
                return i