class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a single list and sort it
        nums = sorted(num for row in grid for num in row)
        
        # Find the median of the sorted list
        median = nums[len(nums) // 2]
        
        # Calculate the total number of operations needed to make all elements equal to the median
        total_operations = sum(abs(num - median) for num in nums)
        
        # Check if the total operations are divisible by x
        return total_operations // x if total_operations % x == 0 else -1