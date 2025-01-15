class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        required_set_bits = bin(num2).count('1')

        result = 0

        for i in range(31, -1, -1):
            if (num1 & (1 << i)) and required_set_bits > 0:
                result |= (1 << i)
                required_set_bits -= 1

        for i in range(32):
            if required_set_bits == 0:
                break
            if not (result & (1 << i)):
                result |= (1 << i)
                required_set_bits -= 1

        return result