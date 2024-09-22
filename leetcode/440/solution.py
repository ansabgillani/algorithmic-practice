class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_numbers(prefix):
            current, next_prefix = prefix, prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        num = 1
        k -= 1
        while k > 0:
            count = count_numbers(num)
            if k < count:
                num *= 10
                k -= 1
            else:
                k -= count
                num += 1
        return num