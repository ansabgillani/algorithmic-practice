import heapq

def kthSmallest(matrix, k):
    """
    Finds the k-th smallest element in a sorted n x n matrix.
    
    Args:
    matrix (List[List[int]]): The input n x n matrix where rows and columns are sorted in ascending order.
    k (int): The k-th position to find the smallest element for.
    
    Returns:
    int: The k-th smallest element in the matrix.
    """
    min_heap = []
    
    # Push the first element of each row into the heap
    for i in range(min(len(matrix), k)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    while k > 1:
        _, row, col = heapq.heappop(min_heap)
        
        # Move to the next element in the same row
        if col + 1 < len(matrix[0]):
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        
        k -= 1
    
    return min_heap[0][0]

# Test cases
assert kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
assert kthSmallest([[-5]], 1) == -5