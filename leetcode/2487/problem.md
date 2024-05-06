# Remove Nodes From Linked List

**Problem ID:** 2487

**Difficulty:** Medium

## Problem Description

Given the head of a linked list, remove every node which has a node with a greater value anywhere to the right side of it. Return the head of the modified linked list.

## Examples

### Example 1
![Example 1 Diagram](https://assets.leetcode.com/uploads/2022/10/02/drawio.png)

**Input:** `head = [5,2,13,3,8]`

**Output:** `[13,8]`

**Explanation:** The nodes that should be removed are 5, 2 and 3.

### Example 2

**Input:** `head = [1,1,1,1]`

**Output:** `[1,1,1,1]`

**Explanation:** Every node has value 1, so no nodes are removed.

## Constraints

- The number of the nodes in the given list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

## Topic Tags
- Linked List
- Stack
- Recursion
- Monotonic Stack