from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    """
    Finds and returns the k closest integers to x in a sorted array.
    
    :param arr: Sorted list of integers.
    :param k: Number of closest elements to return.
    :param x: Target integer.
    :return: List of k closest integers to x, sorted in ascending order.
    """
    # Edge case when k is equal to the length of the array
    if k == len(arr):
        return arr
    
    # Initialize two pointers
    left, right = 0, len(arr) - k
    
    # Perform binary search
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
            
    # Return the subarray from left to left+k
    return arr[left:left+k]