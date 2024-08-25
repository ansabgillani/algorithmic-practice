# Binary Tree Postorder Traversal

**Problem ID:** 145

**Difficulty:** Easy

## Content

Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

### Example 1

**Input:** 
```plaintext
root = [1,null,2,3]


**Output:** 
```plaintext
[3,2,1]


**Explanation:**
![Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

### Example 2

**Input:** 
```plaintext
root = [1,2,3,4,5,null,8,null,null,6,7,9]


**Output:** 
```plaintext
[4,6,7,5,2,9,8,3,1]


**Explanation:**
![Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

### Example 3

**Input:** 
```plaintext
root = []


**Output:** 
```plaintext
[]


### Example 4

**Input:** 
```plaintext
root = [1]


**Output:** 
```plaintext
[1]


## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

### Follow up

Recursive solution is trivial, could you do it iteratively?

## Topic Tags

Stack, Tree, Depth-First Search, Binary Tree