class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Helper function to check if a number is symmetric
        def is_symmetric(x: int) -> bool:
            str_x = str(x)
            n = len(str_x)
            if n % 2 != 0:
                return False
            half = n // 2
            first_half_sum = sum(int(digit) for digit in str_x[:half])
            second_half_sum = sum(int(digit) for digit in str_x[half:])
            return first_half_sum == second_half_sum

        # Count symmetric integers in the range [low, high]
        count = 0
        for x in range(low, high + 1):
            if is_symmetric(x):
                count += 1

        return count