def findUnsortedSubarray(nums):
    """
    Finds the length of the shortest subarray that, when sorted, makes the whole array sorted.
    
    Args:
    nums (List[int]): The input list of integers.
    
    Returns:
    int: The length of the shortest unsorted continuous subarray.
    """
    # Create a copy of the original array and sort it
    sorted_nums = sorted(nums)
    
    # Initialize variables to store the start and end indices of the subarray
    start, end = len(nums), 0
    
    # Iterate through the original array and find the first mismatch from both ends
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            start = min(start, i)
            end = max(end, i)
    
    # If no mismatch is found, return 0 (already sorted)
    if start == len(nums):
        return 0
    
    # Return the length of the subarray
    return end - start + 1

# Example usage:
nums = [2,6,4,8,10,9,15]
print(findUnsortedSubarray(nums))  # Output: 5