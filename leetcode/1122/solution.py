class Solution:
    def relativeSortArray(self, arr1, arr2):
        order = {v: i for i, v in enumerate(arr2)}
        
        def sort_key(x):
            return (order.get(x, float('inf')), x)
        
        return sorted(arr1, key=sort_key)

# Example usage:
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(solution.relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(solution.relativeSortArray(arr1, arr2))  # Output: [22,28,8,6,17,44]