# Maximal Rectangle

**Problem ID:** 85  
**Difficulty:** Hard

## Description
Given a `rows x cols` binary matrix filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

## Example 1:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />
**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 6  
**Explanation:** The maximal rectangle is shown in the above picture.

## Example 2:
**Input:** matrix = [["0"]]
**Output:** 0

## Example 3:
**Input:** matrix = [["1"]]
**Output:** 1

## Constraints
- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`.

## Topic Tags
- Array
- Dynamic Programming
- Stack
- Matrix
- Monotonic Stack