# Binary Search Tree to Greater Sum Tree

**Problem ID:** 1038

**Difficulty:** Medium

## Description
Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

### Constraints
- The number of nodes in the tree is in the range `[1, 100]`.
- `0 <= Node.val <= 100`
- All the values in the tree are unique.

## Example

**Example 1:**
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/02/tree.png" style="width: 400px; height: 273px;" />

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


**Example 2:**

Input: root = [0,null,1]
Output: [1,null,1]


## Solution

### Topic Tags
Tree, Depth-First Search, Binary Search Tree, Binary Tree