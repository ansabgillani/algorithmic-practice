# Sum of Distances in Tree

**Problem ID:** 834

**Difficulty:** Hard

## Problem Description

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges. You are given the integer `n` and the array `edges` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `i-th` node in the tree and all other nodes.

## Examples

**Example 1:**

![lc-sumdist1.jpg]{width=304px height=224px}

**Input:** n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

**Output:** [8,12,6,10,10,10]

**Explanation:**

We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

**Example 2:**

![lc-sumdist2.jpg]{width=64px height=65px}

**Input:** n = 1, edges = []

**Output:** [0]

**Example 3:**

![lc-sumdist3.jpg]{width=144px height=145px}

**Input:** n = 2, edges = [[1,0]]

**Output:** [1,1]

## Constraints

- `1 <= n <= 3 * 10^4`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- The given input represents a valid tree.

## Topic Tags

Dynamic Programming, Tree, Depth-First Search, Graph