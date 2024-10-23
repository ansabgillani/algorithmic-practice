import heapq

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # Calculate the maximum possible sum (sum of all positive numbers)
        max_sum = 0
        for num in nums:
            if num > 0:
                max_sum += num
        
        # Initialize a min heap with the smallest subsequence sum (all negative numbers)
        min_heap = []
        for num in nums:
            if num < 0:
                heapq.heappush(min_heap, (-num, -num))
        
        # Pop the smallest elements and push their partial sums back into the heap
        for _ in range(k-1):
            sum_val, val = heapq.heappop(min_heap)
            if min_heap:
                new_sum = sum_val + min_heap[0][0]
                heapq.heappush(min_heap, (new_sum, -val))
        
        # The kth smallest subsequence sum is the negative of the current top of the heap
        return -min_heap[0][0]

# Example usage:
solution = Solution()
print(solution.kSum([2, 4, -2], 5))  # Output: 2
print(solution.kSum([1, -2, 3, 4, -10, 12], 16))  # Output: 10