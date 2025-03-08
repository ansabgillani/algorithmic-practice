def minimumRecolors(blocks, k):
    """
    :type blocks: str
    :type k: int
    :rtype: int
    """
    min_operations = float('inf')
    count = 0
    
    # Slide the window of size k across the string
    for i in range(len(blocks)):
        if blocks[i] == 'W':
            count += 1
        if i >= k and blocks[i - k] == 'W':
            count -= 1
        if i >= k - 1:
            min_operations = min(min_operations, count)
    
    return min_operations

# Example usage:
print(minimumRecolors("WBBWWBBWBW", 7))  # Output: 3
print(minimumRecolors("WBWBBBW", 2))     # Output: 0