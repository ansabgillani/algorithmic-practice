class Solution:
    def smallestRange(self, nums):
        max_val = -float('inf')
        heap = []
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
    
        smallest_range = [heap[0][0], max_val]
        
        while True:
            current_min, list_idx, element_idx = heapq.heappop(heap)
            
            if element_idx == len(nums[list_idx]) - 1:
                break
            
            next_element = nums[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))
            max_val = max(max_val, next_element)
            
            if max_val - heap[0][0] < smallest_range[1] - smallest_range[0]:
                smallest_range = [heap[0][0], max_val]
        
        return smallest_range