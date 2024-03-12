# Remove Zero Sum Consecutive Nodes from Linked List

**Problem ID:** 1171

**Difficulty:** Medium

## Description
Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences. After doing so, return the head of the final linked list.

## Examples
### Example 1:
```plaintext
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.


### Example 2:
```plaintext
Input: head = [1,2,3,-3,4]
Output: [1,2,4]


### Example 3:
```plaintext
Input: head = [1,2,3,-3,-2]
Output: [1]


## Constraints
- The given linked list will contain between `1` and `1000` nodes.
- Each node in the linked list has `-1000 <= node.val <= 1000`.

## Topic Tags
Hash Table, Linked List