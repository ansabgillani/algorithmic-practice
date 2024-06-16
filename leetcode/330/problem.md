# Patching Array

**Problem ID:** 330  
**Difficulty:** Hard

## Problem Description

Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

## Examples

### Example 1
**Input:** nums = [1,3], n = 6  
**Output:** 1  
**Explanation:** By adding/patching 2 to `nums`, the combinations cover the range `[1, 6]`.

### Example 2
**Input:** nums = [1,5,10], n = 20  
**Output:** 2  
**Explanation:** The two patches can be [2, 4].

### Example 3
**Input:** nums = [1,2,2], n = 5  
**Output:** 0

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `nums` is sorted in ascending order.
- `1 <= n <= 2^31 - 1`

## Topic Tags
Array, Greedy