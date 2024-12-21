# Maximum Number of K-Divisible Components

**Problem ID:** 2872

**Difficulty:** Hard

## Description
Given an undirected tree with `n` nodes labeled from `0` to `n - 1`, and a 2D integer array `edges` representing the edges between nodes, along with a 0-indexed integer array `values` where `values[i]` is the value associated with the `i-th` node. Also given an integer `k`. A valid split of the tree is obtained by removing any set of edges (possibly empty) such that all resulting components have values divisible by `k`.

Return the maximum number of components in any valid split.

## Examples

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg" style="width: 1024px; height: 453px;" />

```plaintext
Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
Output: 2
Explanation: The split removes the edge connecting node 1 with 2. The resulting components are valid because:
- The component containing nodes 1 and 3 has a value of values[1] + values[3] = 12.
- The component containing nodes 0, 2, and 4 has a value of values[0] + values[2] + values[4] = 6.


**Example 2:**

<img src="https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg" style="width: 999px; height: 338px;" />

```plaintext
Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
Output: 3
Explanation: The split removes the edge connecting node 0 with 2 and the edge connecting node 0 with 1. The resulting components are valid because:
- The component containing node 0 has a value of values[0] = 3.
- The component containing nodes 2, 5, and 6 has a value of values[2] + values[5] + values[6] = 9.
- The component containing nodes 1, 3, and 4 has a value of values[1] + values[3] + values[4] = 6.


## Constraints
- `1 <= n <= 3 * 10^4`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `values.length == n`
- `0 <= values[i] <= 10^9`
- `1 <= k <= 10^9`
- Sum of `values` is divisible by `k`.
- The input is generated such that `edges` represents a valid tree.

## Topic Tags
Tree, Depth-First Search