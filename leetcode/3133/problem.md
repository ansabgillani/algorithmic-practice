# Minimum Array End

**Problem ID:** 3133

**Difficulty:** Medium

## Description
Given two integers `n` and `x`, construct an array of **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1] > nums[i]`, and the result of the bitwise **AND** operation between all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.

## Example

### Example 1
- **Input:** n = 3, x = 4
- **Output:** 6
- **Explanation:** nums can be [4,5,6] and its last element is 6.

### Example 2
- **Input:** n = 2, x = 7
- **Output:** 15
- **Explanation:** nums can be [7,15] and its last element is 15.

## Constraints

- `1 <= n, x <= 10^8`

## Topic Tags
- Bit Manipulation