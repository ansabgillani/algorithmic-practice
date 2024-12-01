def checkIfExist(arr):
    """
    Check if there exists two indices i and j such that arr[i] == 2 * arr[j].
    
    :type arr: List[int]
    :rtype: bool
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num * 2)
        if num % 2 == 0:
            seen.add(num // 2)
    return False

# Test cases
print(checkIfExist([10, 2, 5, 3]))  # Output: true
print(checkIfExist([3, 1, 7, 11]))  # Output: false