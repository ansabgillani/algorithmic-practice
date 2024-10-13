import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize min heap and current maximum value
        min_heap = []
        current_max = float('-inf')
        
        # Push the first element of each list into the heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        smallest_range = [min_heap[0][0], current_max]
        
        # Process the heap until we can't get a smaller range
        while True:
            _, i, j = heapq.heappop(min_heap)
            
            if j + 1 == len(nums[i]):
                break
            
            next_value = nums[i][j + 1]
            heapq.heappush(min_heap, (next_value, i, j + 1))
            current_max = max(current_max, next_value)
            
            # Update the smallest range
            if current_max - min_heap[0][0] < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_heap[0][0], current_max]
        
        return smallest_range

# Example usage:
# solution = Solution()
# print(solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])) # Output: [20, 24]