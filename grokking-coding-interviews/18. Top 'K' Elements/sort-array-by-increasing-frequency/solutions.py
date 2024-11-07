def frequencySort(nums):
    # Count the frequency of each number
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Sort the numbers first by increasing frequency, then by decreasing value
    sorted_nums = sorted(nums, key=lambda x: (count[x], -x))
    
    return sorted_nums

# Test cases to verify the solution
print(frequencySort([1,1,2,2,2,3]))  # Output: [3,1,1,2,2,2]
print(frequencySort([2,3,1,3,2]))    # Output: [1,3,3,2,2]
print(frequencySort([-1,1,-6,4,5,-6,1,4,1]))  # Output: [5,-1,4,4,-6,-6,1,1,1]