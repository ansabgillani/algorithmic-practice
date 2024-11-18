class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n

        if k > 0:
            total = sum(code[:k])
            for i in range(n):
                result[i] = total
                total += code[(i + k) % n]
                total -= code[i]
        elif k < 0:
            total = sum(code[k:])
            for i in range(n):
                result[i] = total
                total += code[i]
                total -= code[(i - k) % n]

        return result