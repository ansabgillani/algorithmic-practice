class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        set_bits_num2 = num2.bit_count()
        
        # Initialize result and bit position counter
        result = 0
        bit_position = 0
        
        # Iterate over each bit position from the most significant to the least significant
        while num1 > 0 or set_bits_num2 > 0:
            # Check if the current bit of num1 is set
            if num1 & 1 == 1 and set_bits_num2 > 0:
                # Set the corresponding bit in result
                result |= (1 << bit_position)
                set_bits_num2 -= 1
            # Move to the next bit position
            bit_position += 1
            # Right shift num1 by 1 to check the next bit
            num1 >>= 1
        
        # If there are remaining set bits to be placed, place them in the least significant bits of result
        while set_bits_num2 > 0:
            result |= (1 << bit_position)
            bit_position += 1
            set_bits_num2 -= 1
        
        return result

# Test cases
solution = Solution()
print(solution.minimizeXor(3, 5))  # Output: 3
print(solution.minimizeXor(1, 12))  # Output: 3