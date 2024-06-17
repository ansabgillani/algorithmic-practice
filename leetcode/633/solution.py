class Solution:
    def judgeSquareSum(self, c):
        i = 0
        while i * i <= c:
            j = int((c - i * i) ** 0.5)
            if i * i + j * j == c:
                return True
            i += 1
        return False