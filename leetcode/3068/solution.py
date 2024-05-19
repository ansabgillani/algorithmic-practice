class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Calculate the sum without any operations
        total_sum = sum(nums)
        # Calculate the potential increase if we apply XOR operation on each number
        increases = [(num ^ k) - num for num in nums]
        # Find the maximum possible increase from applying XOR to any subset of nodes
        max_increase = max(sum(sorted(increases)[-2:]), 0)
        
        return total_sum + max_increase