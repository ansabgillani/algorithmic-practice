# Count Subarrays With Fixed Bounds

**Problem ID:** 2444

**Difficulty:** Hard

## Description
Given an integer array `nums` and two integers `minK` and `maxK`, a **fixed-bound subarray** of `nums` is defined as a subarray that satisfies the following conditions:

- The **minimum** value in the subarray is equal to `minK`.
- The **maximum** value in the subarray is equal to `maxK`.

Return _the number_ of fixed-bound subarrays.

A **subarray** is a contiguous part of an array.

## Example

**Example 1:**

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].


**Example 2:**

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


## Constraints

- `2 <= nums.length <= 10^5`
- `1 <= nums[i], minK, maxK <= 10^6`

## Topic Tags

Array, Queue, Sliding Window, Monotonic Queue