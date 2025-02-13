import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert nums into a min-heap in-place
        heapq.heapify(nums)
        
        operations = 0
        
        while nums[0] < k:
            # Pop the two smallest elements from the heap
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Compute the new element and push it back into the heap
            new_element = (min(x, y) * 2 + max(x, y))
            heapq.heappush(nums, new_element)
            
            # Increment the operation count
            operations += 1
        
        return operations

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.minOperations([2, 11, 10, 1, 3], k=10))  # Output: 2
    print(solution.minOperations([1, 1, 2, 4, 9], k=20))  # Output: 4