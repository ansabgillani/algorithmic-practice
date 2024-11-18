class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        if k == 0:
            return result
        
        if k > 0:
            window_sum = sum(code[:k])
            for i in range(n):
                result[i] = window_sum
                window_sum += code[(i + k) % n] - code[i]
        else:
            k = -k
            window_sum = sum(code[-k:])
            for i in range(n):
                result[i] = window_sum
                window_sum += code[i] - code[(n - k + i) % n]
        
        return result