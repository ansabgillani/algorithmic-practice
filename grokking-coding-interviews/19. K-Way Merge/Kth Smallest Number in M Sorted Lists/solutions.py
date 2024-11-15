from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, arr: List[List[int]], m: int) -> int:
        """
        Finds the m-th smallest element in k sorted arrays.
        
        Parameters:
        arr (List[List[int]]): A list of k sorted lists.
        m (int): The order of the smallest element to find.
        
        Returns:
        int: The m-th smallest element in the merged array.
        """
        min_heap = []
        # Initialize the heap with the first element of each array
        for i, a in enumerate(arr):
            if a:
                heappush(min_heap, (a[0], i, 1))
        
        # Extract elements from the heap m times
        for _ in range(m-1):
            val, row_idx, col_idx = heappop(min_heap)
            if col_idx < len(arr[row_idx]):
                heappush(min_heap, (arr[row_idx][col_idx], row_idx, col_idx + 1))
        
        return min_heap[0][0]