class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions to facilitate the binary search
        position.sort()
        
        n = len(position)
        
        # Helper function to check if we can place m balls with at least 'mid' distance between them
        def can_place(mid):
            count = 1
            last_position = position[0]
            for i in range(1, n):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]
                if count == m:
                    return True
            return False
        
        # Binary search to find the maximum minimum distance
        left, right = 0, position[-1] - position[0]
        best_mid = 0
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                best_mid = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best_mid

# Example usage:
# solution = Solution()
# print(solution.maxDistance([1,2,3,4,7], 3))  # Output: 3
# print(solution.maxDistance([5,4,3,2,1,1000000000], 2))  # Output: 999999999