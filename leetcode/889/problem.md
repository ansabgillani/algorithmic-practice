# Construct Binary Tree from Preorder and Postorder Traversal

**Problem ID:** 889

**Difficulty:** Medium

## Description
Given two integer arrays, `preorder` and `postorder` where `preorder` is the preorder traversal of a binary tree of **distinct** values and `postorder` is the postorder traversal of the same tree, reconstruct and return **the binary tree**.

If there exist multiple answers, you can **return any** of them.

## Examples
### Example 1
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg" style="width: 304px; height: 265px;" />
```plaintext
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


### Example 2
```plaintext
Input: preorder = [1], postorder = [1]
Output: [1]


## Constraints
- `1 <= preorder.length <= 30`
- `1 <= preorder[i] <= preorder.length`
- All the values of `preorder` are **unique**.
- `postorder.length == preorder.length`
- `1 <= postorder[i] <= postorder.length`
- All the values of `postorder` are **unique**.
- It is guaranteed that `preorder` and `postorder` are the preorder traversal and postorder traversal of the same binary tree.

## Topic Tags
- Array
- Hash Table
- Divide and Conquer
- Tree
- Binary Tree