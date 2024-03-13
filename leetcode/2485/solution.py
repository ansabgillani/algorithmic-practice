class Solution:
    def pivotInteger(self, n):
        total_sum = n * (n + 1) // 2
        left_sum = 0

        for x in range(1, n+1):
            right_sum = total_sum - left_sum - x
            if left_sum == right_sum:
                return x
            left_sum += x
        
        return -1