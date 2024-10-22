# Kth Largest Sum in a Binary Tree

**Problem ID:** 2583

**Difficulty:** Medium

## Description
Given the `root` of a binary tree and a positive integer `k`, return the `k`<sup>th</sup> largest level sum in the tree (not necessarily distinct). If there are fewer than `k` levels, return `-1`.

**Note:** Two nodes are on the same level if they have the same distance from the root.

## Example
### Example 1
![Example 1 Diagram](https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png)
```plaintext
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are as follows:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.


### Example 2
![Example 2 Diagram](https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png)
```plaintext
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.


## Constraints
- The number of nodes in the tree is `n`.
- `2 <= n <= 10^5`
- `1 <= Node.val <= 10^6`
- `1 <= k <= n`

## Topic Tags
Tree, Breadth-First Search, Sorting, Binary Tree