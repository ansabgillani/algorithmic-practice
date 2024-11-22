import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Finds the smallest range that includes at least one number from each of k sorted lists.
        
        :param nums: List of k sorted lists of integers.
        :return: Smallest range as a list [a, b].
        """
        # Initialize heap with first element of each list and keep track of max value
        min_heap = []
        current_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], 0, nums[i]))
            current_max = max(current_max, nums[i][0])
        
        # Initialize the smallest range with a large value
        start, end = min_heap[0][0], current_max
        
        while True:
            # Extract the minimum element from the heap
            val, idx, lst = heapq.heappop(min_heap)
            
            # If this is the last element of any list, break
            if idx == len(lst) - 1:
                break
            
            # Move to the next element in the current list
            next_val = lst[idx + 1]
            heapq.heappush(min_heap, (next_val, idx + 1, lst))
            
            # Update the current max value
            current_max = max(current_max, next_val)
            
            # Check if the new range is smaller than the previous one
            if current_max - min_heap[0][0] < end - start:
                start, end = min_heap[0][0], current_max
        
        return [start, end]

# Example usage
solution = Solution()
print(solution.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))  # Output: [20, 24]
print(solution.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))  # Output: [1, 1]