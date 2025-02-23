# Name: 
Missing Number

## Difficulty: 
Easy

## Description: 
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Example 1:**

- **Input:** `nums = [3,0,1]`
- **Output:** `2`

**Explanation:**
Since `n = 3`, all numbers should be in the range `[0,3]`. The number `2` is missing since it does not appear in `nums`.

**Example 2:**

- **Input:** `nums = [0,1]`
- **Output:** `2`

**Explanation:**
Since `n = 2`, all numbers should be in the range `[0,2]`. The number `2` is missing since it does not appear in `nums`.

**Example 3:**

- **Input:** `nums = [9,6,4,2,3,5,7,0,1]`
- **Output:** `8`

**Explanation:**
Since `n = 9`, all numbers should be in the range `[0,9]`. The number `8` is missing since it does not appear in `nums`.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are unique.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?