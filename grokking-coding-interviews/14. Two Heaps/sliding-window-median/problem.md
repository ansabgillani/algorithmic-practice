# Sliding Window Median

## Difficulty: 
Hard

## Description: 
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which moves from the very left to the very right of the array. You can only see the `k` numbers in the window at any time. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within \(10^{-5}\) of the actual value will be accepted.

### Example 1:
#### Input:
- `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`

#### Output:
- `[1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]`

### Example 2:
#### Input:
- `nums = [1,2,3,4,2,3,1,4,2]`, `k = 3`

#### Output:
- `[2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]`

### Constraints:
- `1 <= k <= nums.length <= 10^5`
- `-2^{31} <= nums[i] <= 2^{31} - 1`