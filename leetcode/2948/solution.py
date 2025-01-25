def lexicographicallySmallestArray(nums, limit):
    """
    Sorts the array in such a way that it becomes lexicographically smallest by swapping elements where the absolute difference is less than or equal to the limit.
    
    :param nums: List[int] - The input list of positive integers
    :param limit: int - The maximum allowed difference for swapping elements
    :return: List[int] - The lexicographically smallest array
    """
    n = len(nums)
    indices = sorted(range(n), key=lambda i: nums[i])
    
    ans = [0] * n
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        
        start = i
        while start < n and abs(nums[indices[start]] - nums[indices[(start + 1) % n]]) <= limit:
            start += 1
        
        subarray = indices[i:start]
        subarray.sort()
        
        for j, idx in enumerate(subarray):
            ans[idx] = nums[subarray[j]]
            visited[idx] = True
    
    return ans

# Example usage:
# print(lexicographicallySmallestArray([1,5,3,9,8], 2))  # Output: [1,3,5,8,9]
# print(lexicographicallySmallestArray([1,7,6,18,2,1], 3))  # Output: [1,6,7,18,1,2]
# print(lexicographicallySmallestArray([1,7,28,19,10], 3))  # Output: [1,7,28,19,10]