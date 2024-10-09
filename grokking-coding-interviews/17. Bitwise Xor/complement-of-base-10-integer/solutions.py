class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Given a non-negative integer n, this method returns its bitwise complement.
        
        :param n: Non-negative integer whose bitwise complement is to be found
        :return: Bitwise complement of the given integer
        """
        # Edge case: if n is 0, return 1 as the complement of 0 is 1
        if n == 0:
            return 1
        
        # Calculate the number of bits required to represent n in binary
        num_bits = n.bit_length()
        
        # Create a mask with all bits set to 1 of the same length as n
        mask = (1 << num_bits) - 1
        
        # XOR n with the mask to get its bitwise complement
        return n ^ mask

# Test cases to verify the correctness of the solution
def test_bitwiseComplement():
    assert Solution().bitwiseComplement(5) == 2, "Test case 1 failed"
    assert Solution().bitwiseComplement(7) == 0, "Test case 2 failed"
    assert Solution().bitwiseComplement(10) == 5, "Test case 3 failed"
    print("All test cases passed!")

# Run the test function
test_bitwiseComplement()