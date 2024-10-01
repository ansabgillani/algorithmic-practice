class Solution:
    def canArrange(self, arr, k):
        remainder_counts = [0] * k
        for num in arr:
            remainder_counts[num % k] += 1
        
        if remainder_counts[0] % 2 != 0:
            return False
        
        for i in range(1, (k // 2) + 1):
            if remainder_counts[i] != remainder_counts[k - i]:
                return False

        return True