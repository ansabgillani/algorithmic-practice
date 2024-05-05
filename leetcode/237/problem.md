# Delete Node in a Linked List

**Problem ID:** 237

**Difficulty:** Medium

## Content
Given a singly-linked list `head` and a node to be deleted `node`, delete the given node from the linked list. You will **not be given access** to the first node of `head`. All values in the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.

### Requirements
- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before `node` should be in the same order.
- All the values after `node` should be in the same order.

### Example 1

**Input:**

head = [4,5,1,9], node = 5


**Output:**

[4,1,9]


**Explanation:** 
You are given the second node with value `5`, the linked list should become `4 -> 1 -> 9` after calling your function.

### Example 2

**Input:**

head = [4,5,1,9], node = 1


**Output:**

[4,5,9]


**Explanation:** 
You are given the third node with value `1`, the linked list should become `4 -> 5 -> 9` after calling your function.

### Constraints

- The number of nodes in the given list is in the range `[2, 1000]`.
- `-1000 <= Node.val <= 1000`
- The value of each node in the list is unique.
- The `node` to be deleted is in the list and is not a tail node.

## Topic Tags
Linked List