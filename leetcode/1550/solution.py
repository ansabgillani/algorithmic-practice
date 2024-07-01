def threeConsecutiveOdds(arr):
    """
    Check if there are three consecutive odd numbers in the array.
    
    :param arr: List[int] - The input integer array.
    :return: bool - True if there are three consecutive odd numbers, False otherwise.
    """
    # Iterate through the array, stopping at the third last element
    for i in range(len(arr) - 2):
        # Check if the current and next two elements are all odd
        if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
            return True
    return False

# Test cases to verify the solution
print(threeConsecutiveOdds([2, 6, 4, 1]))  # Output: False
print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Output: True