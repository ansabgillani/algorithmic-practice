from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k <= 0:
            return []
        
        window = SortedList(nums[:k])
        result = [window[k // 2] * 0.5 + window[(k - 1) // 2] * 0.5]
        
        for i in range(k, len(nums)):
            window.add(nums[i])
            window.remove(nums[i - k])
            median = window[k // 2] * 0.5 + window[(k - 1) // 2] * 0.5
            result.append(median)
            
        return result

# Example usage:
sol = Solution()
print(sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
print(sol.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))  # Output: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]