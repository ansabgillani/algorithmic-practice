import heapq

class KthLargest:
    def __init__(self, k: int, nums):
        """
        Initializes the object with the integer k and the stream of test scores nums.
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        """
        Adds a new test score val to the stream and returns the element representing 
        the kth largest element in the pool of test scores so far.
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

# Example usage:
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8

kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(kthLargest.add(2))  # Output: 7
print(kthLargest.add(10)) # Output: 7
print(kthLargest.add(9))  # Output: 7
print(kthLargest.add(9))  # Output: 8