class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Dictionary to store the prefix XOR and its indices
        prefix_xor_indices = {0: [-1]}
        xor_sum = 0
        triplet_count = 0
        
        for i, num in enumerate(arr):
            xor_sum ^= num
            if xor_sum in prefix_xor_indices:
                # For each previous occurrence of this XOR sum,
                # all indices between the current and previous can form valid triplets with j=i+1
                triplet_count += i * (i - 1) // 2 - sum(prefix_xor_indices[xor_sum])
                prefix_xor_indices[xor_sum].append(i)
            else:
                prefix_xor_indices[xor_sum] = [i]
        
        return triplet_count

# Test cases to verify the solution
def test_solution():
    assert Solution().countTriplets([2, 3, 1, 6, 7]) == 4
    assert Solution().countTriplets([1, 1, 1, 1, 1]) == 10
    print("All tests passed.")

test_solution()