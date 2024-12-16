import heapq

class Solution:
    def finalArray(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Perform k operations on nums where each operation involves finding the minimum value,
        replacing it with that value multiplied by the multiplier.
        
        :param nums: List of integers to be modified
        :param k: Number of operations to perform
        :param multiplier: Value by which the minimum element is multiplied in each operation
        :return: Final state of nums after all operations
        """
        # Convert nums into a min-heap for efficient retrieval and updates
        heapq.heapify(nums)
        
        # Perform k operations
        for _ in range(k):
            # Extract the smallest element from the heap
            min_val = heapq.heappop(nums)
            # Multiply it by the multiplier
            min_val *= multiplier
            # Push the updated value back into the heap
            heapq.heappush(nums, min_val)
        
        return nums