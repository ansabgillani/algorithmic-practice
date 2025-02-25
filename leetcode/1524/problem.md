# Number of Sub-arrays With Odd Sum

**Problem ID:** 1524

**Difficulty:** Medium

## Description
Given an array of integers `arr`, return the number of subarrays with an **odd** sum.

Since the answer can be very large, return it modulo \(10^9 + 7\).

## Examples

**Example 1:**


Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.


**Example 2:**


Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays have even sum and the answer is 0.


**Example 3:**


Input: arr = [1,2,3,4,5,6,7]
Output: 16


## Constraints

- \(1 \leq arr.length \leq 10^5\)
- \(1 \leq arr[i] \leq 100\)

## Topic Tags

- Array
- Math
- Dynamic Programming
- Prefix Sum