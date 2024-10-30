import heapq

def findKthLargest(nums, k):
    """
    Finds the kth largest element in the given array nums.
    
    Args:
    nums: List[int] - A list of integers.
    k: int - The order of the largest element to find.
    
    Returns:
    int - The kth largest element in nums.
    """
    # Use a min-heap to keep track of the top k elements
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

# Test cases
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4