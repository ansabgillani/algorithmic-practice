# Smallest String Starting From Leaf

**Problem ID:** 988  
**Difficulty:** Medium

## Description
Given the `root` of a binary tree where each node has a value in the range `[0, 25]` representing the letters `'a'` to `'z'`, return the **lexicographically smallest** string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is **lexicographically smaller**. A leaf of a node is a node that has no children.

## Examples
### Example 1
![Tree1](https://assets.leetcode.com/uploads/2019/01/30/tree1.png)

Input: root = [0,1,2,3,4,3,4]
Output: "dba"


### Example 2
![Tree2](https://assets.leetcode.com/uploads/2019/01/30/tree2.png)

Input: root = [25,1,3,1,3,0,2]
Output: "adz"


### Example 3
![Tree3](https://assets.leetcode.com/uploads/2019/02/01/tree3.png)

Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"


## Constraints
- The number of nodes in the tree is in the range `[1, 8500]`.
- `0 <= Node.val <= 25`

## Topic Tags
- String
- Backtracking
- Tree
- Depth-First Search
- Binary Tree