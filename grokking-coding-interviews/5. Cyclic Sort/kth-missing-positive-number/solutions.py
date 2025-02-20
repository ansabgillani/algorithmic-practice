class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize binary search bounds
        left, right = 0, len(arr)
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            # Calculate the number of missing positive numbers up to arr[mid]
            missing = arr[mid] - mid - 1
            
            if missing < k:
                # If there are fewer than k missing numbers, move to the right half
                left = mid + 1
            else:
                # Otherwise, move to the left half
                right = mid
        
        # The k-th missing positive number is in the range (left-1, left]
        return left + k - 1