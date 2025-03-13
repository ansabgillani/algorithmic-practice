class Solution:
    def minOperations(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        max_val = max(nums)
        
        # Create a frequency array to count occurrences of each value in nums
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        
        # Prefix sum array to quickly calculate the number of elements <= x
        prefix_sum = list(accumulate(freq, initial=0))
        
        k = 0
        for l, r, val in queries:
            k += 1
            
            # Calculate the total decrement needed for the range [l, r]
            total_decrement_needed = prefix_sum[r + 1] - prefix_sum[l]
            
            if total_decrement_needed > val * (r - l + 1):
                return -1
            
            # Apply the decrement to the frequency array
            freq[max_val + 1] += val
            freq[min(max_val, r) + 1] -= val
            prefix_sum = list(accumulate(freq, initial=0))
        
        return k