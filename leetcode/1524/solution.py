class Solution:
    def numOfSubarrays(self, arr):
        odd_count = even_count = result = 0
        mod = 10**9 + 7

        for num in arr:
            if num % 2 == 0:
                result += even_count
                even_count += 1
            else:
                result += odd_count + 1
                odd_count, even_count = even_count + 1, odd_count

        return result % mod