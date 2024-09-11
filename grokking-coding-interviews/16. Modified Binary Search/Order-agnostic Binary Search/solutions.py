class Solution:
    def binarySearch(self, arr: List[int], target: int) -> int:
        """
        Perform order-agnostic binary search on a sorted array to find the target element.
        
        :param arr: List of integers, sorted in ascending or descending order
        :param target: Integer, the target element to search for
        :return: Index of the target element if found, otherwise -1
        """
        start, end = 0, len(arr) - 1
        
        # Determine the direction of sorting
        is_ascending = arr[start] < arr[end]
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid] == target:
                return mid
            elif is_ascending:
                if arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if arr[mid] > target:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1

# Example usage:
sol = Solution()
print(sol.binarySearch([40, 10, 5, 2, 1], 10))  # Output: 1
print(sol.binarySearch([1], 10))                  # Output: -1