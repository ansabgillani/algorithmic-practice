class Solution:
    def maxKelements(self, nums, k):
        import heapq
        from math import ceil

        # Convert the list into a max heap by negating each element
        nums = [-n for n in nums]
        heapq.heapify(nums)
        
        # Perform operations
        score = 0
        for _ in range(k):
            # Get the largest element (negated back to positive)
            num = -heapq.heappop(nums)
            score += num
            # Push the modified number back into the heap (negated again)
            heapq.heappush(nums, -ceil(num / 3))
        
        return score