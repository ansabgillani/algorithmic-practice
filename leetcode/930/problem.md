# Binary Subarrays With Sum

**Problem ID:** 930

**Difficulty:** Medium

## Description
Given a binary array `nums` and an integer `goal`, return the number of non-empty **subarrays** with a sum equal to `goal`.

A **subarray** is a contiguous part of the array.

## Examples
### Example 1:
**Input:** nums = [1,0,1,0,1], goal = 2  
**Output:** 4  

**Explanation:**
The 4 subarrays are bolded and underlined below:
[<u><strong>1,0,1</strong></u>,0,1]  
[<u><strong>1,0,1,0</strong></u>,1]  
[1,<u><strong>0,1,0,1</strong></u>]  
[1,0,<u><strong>1,0,1</strong></u>]

### Example 2:
**Input:** nums = [0,0,0,0,0], goal = 0  
**Output:** 15  

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `nums[i]` is either `0` or `1`.
- `0 <= goal <= nums.length`

## Topic Tags
Array, Hash Table, Sliding Window, Prefix Sum