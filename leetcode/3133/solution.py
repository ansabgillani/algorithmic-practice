class Solution:
    def minArrayEnd(self, n: int, x: int) -> int:
        # Initialize the last element of the array as x
        nums = [x]
        
        # Calculate the number of elements needed to fill the array
        remaining = n - 1
        
        # Iterate to construct the array with increasing values
        while remaining > 0:
            # Increment the last element to make it greater than the previous one
            nums[-1] += 1
            
            # Ensure the bitwise AND operation of all elements is still x
            if nums[-1] & x == x:
                remaining -= 1
        
        # Return the minimum possible value of nums[n-1]
        return nums[-1]

# Test cases
solution = Solution()
print(solution.minArrayEnd(3, 4))  # Output: 6
print(solution.minArrayEnd(2, 7))  # Output: 15