class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Initialize variables to track the number of operations and the current flip state
        operations = 0
        n = len(nums)
        
        # Iterate through the array with a sliding window of size 3
        for i in range(n - 2):
            # If the first element of the triplet is not 1, we need to flip it
            if nums[i] == 0:
                operations += 1
                # Flip the next three elements
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]
        
        # After processing, check if the last two elements are 1
        if nums[-2] == 1 and nums[-1] == 1:
            return operations
        else:
            return -1