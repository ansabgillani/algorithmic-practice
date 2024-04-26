# Minimum Falling Path Sum II

**Problem ID:** 1289

**Difficulty:** Hard

## Content

Given an `n x n` integer matrix `grid`, return the minimum sum of a **falling path with non-zero shifts**.

A **falling path with non-zero shifts** is a choice of exactly one element from each row of `grid` such that no two elements chosen in adjacent rows are in the same column.

&nbsp;

**Example 1:**

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/falling-grid.jpg" style="width: 244px; height: 245px;" />

<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is&nbsp;[1,5,7], so the answer is&nbsp;13.
</pre>

**Example 2:**

<pre>
<strong>Input:</strong> grid = [[7]]
<strong>Output:</strong> 7
</pre>

&nbsp;

**Constraints:**

- `n == grid.length == grid[i].length`
- `1 &lt;= n &lt;= 200`
- `-99 &lt;= grid[i][j] &lt;= 99`

## Topic Tags

- Array
- Dynamic Programming
- Matrix